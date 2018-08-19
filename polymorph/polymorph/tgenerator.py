# File from polymorph project
# Copyright (C) 2018 Santiago Hernandez Ramos <shramos@protonmail.com>
# For more information about the project: https://github.com/shramos/polymorph

from collections import OrderedDict
from scapy.all import rdpcap
from pyshark import FileCapture
from polymorph.tfield import TField
from polymorph.template import Template
from polymorph.tlayer import TLayer


class TGenerator(object):
    """This class is responsible for generating the templates from scapy
    packages and completing the remaining layers with the dissectors of
    tshark through pyshark."""

    def __init__(self, pcapfile, scapy_pkts=None, tshark_pkts=None):
        """Initialization method of the class.

        Parameters
        ----------
        pcapfile : str
            Path to a previously captured pcap.
        scapy_pkts : :obj:`PacketList`
            List of packets generated by Scapy.
        tshark_pkts : :obj:`FileCapture`
            List of packets generated by Pyshark.

        """
        if scapy_pkts:
            self._scapy_pkts = scapy_pkts
        else:
            self._scapy_pkts = rdpcap(pcapfile)
        if tshark_pkts:
            self._tshark_pkts = tshark_pkts
        else:
            self._tshark_pkts = FileCapture(pcapfile)
        self._i = -1

    def __del__(self):
        self._tshark_pkts.close()

    def __iter__(self):
        return self

    def __next__(self):
        """Generates a list of templates from a pcap file combining scapy and
        tshark dissectors.

        Returns
        -------
        :obj:`Template`
            A `Template` generated from the packets.

        """
        if self._i == len(self._scapy_pkts) - 1:
            # Closing the file
            self._tshark_pkts.close()
            raise StopIteration
        else:
            self._i += 1
            return self.tgenerate(self._scapy_pkts[self._i],
                                  self._tshark_pkts[self._i],
                                  self._name(self._scapy_pkts[self._i]))

    def tgenerate(self, scapy_pkt, tshark_pkt, name):
        """Generates a template from a scapy and tshark packet.

        Parameters
        ----------
        scapy_pkt : :obj:``
            The packet generated by Scapy.
        tshark_pkt : :obj:``
            The packet generated by Pyshark.
        name : str
            The name of the `Template`.

        Returns
        -------
        :obj: `Template`
            The `Tempalate` generated from the packets.

        """
        raw = bytes(scapy_pkt).hex()
        pkt_len = len(scapy_pkt)
        template = Template(name, raw=raw)
        # Adding the layers that scapy is able to dissect to the template
        for l in self._getlayers(scapy_pkt):
            offset = pkt_len - len(l)
            lslice = str(slice(offset, pkt_len)).encode().hex()
            layer = TLayer(name=l.__class__.__name__, lslice=lslice, raw=raw)
            for f in self._scapyfields(l, offset, scapy_pkt, layer):
                layer.addfield(f)
            template.addlayer(layer)
        # Adding layers that scapy is not able to dissect using tshark
        if scapy_pkt.lastlayer().name == "Raw":
            nlayers = len(list(self._getlayers(scapy_pkt)))
            for l in tshark_pkt.layers[nlayers - 1:]:
                # Use it in case you want to delete scapy layers
                # offset = len(scapy_pkt) - len(raw)
                offset = 0
                fields_slices = self._slices(l, offset)
                if fields_slices:
                    lslice = str(slice(fields_slices[0][1].start, pkt_len)).encode().hex()
                else:
                    lslice = str(slice(pkt_len - len(scapy_pkt['Raw']), pkt_len)).encode().hex()
                layer = TLayer(
                    name="Raw." + str(l.layer_name.upper()), lslice=lslice, raw=raw, custom=True)
                for f in self._tsharkfields(tshark_pkt, l, scapy_pkt, fields_slices, layer):
                    layer.addfield(f)
                template.addlayer(layer)
        return template

    def _scapyfields(self, layer, offset, spkt, tlayer):
        """Generates template fields for a given scapy layer."""
        fdissect = self._dissect_fields(layer, offset)
        raw = bytes(spkt)
        for f in layer.fields_desc:
            # Obtain the scapy repr of the field
            frepr = layer.getfieldval(f.name)
            # Extract the type of the field
            if type(frepr) is int:
                ftype = (int, 'big')
            else:
                frepr = str(frepr)
                ftype = (str, None)
            # Initialization of the field
            field = TField(name=str(f.name),
                           value=raw[
                               eval(fdissect[f.name])],
                           raw=raw.hex(),
                           tslice=fdissect[f.name].encode().hex(),
                           custom=False,
                           size=eval(fdissect[f.name]).stop -
                                eval(fdissect[f.name]).start,
                           frepr=frepr,
                           ftype=ftype,
                           layer=tlayer)
            yield field

    def _tsharkfields(self, tshark_pkt, layer, scapy_pkt, fields_slices, tlayer):
        """Returns the layers of a pyshark package."""
        raw = bytes(scapy_pkt)
        for sl in fields_slices:
            # Obtain the tshark repr of the field
            field = layer.get_field(sl[0])
            frepr = layer.get_field_value(sl[0])
            # Extract the type of the field
            if field.isdecimal():
                frepr = int(frepr)
                ftype = (int, 'big')
            else:
                frepr = str(frepr)
                ftype = (str, None)
            # Initialization of the tfield
            field = TField(name="_".join(sl[0].split('.')[1:]),
                           value=raw[sl[1]],
                           raw=raw.hex(),
                           tslice=str(sl[1]).encode().hex(),
                           custom=True,
                           size=sl[1].stop - sl[1].start,
                           ftype=ftype,
                           frepr=frepr,
                           layer=tlayer)
            yield field

    @staticmethod
    def _getlayers(pkt):
        """Returns the layers of a scapy package."""
        yield pkt
        while pkt.payload:
            pkt = pkt.payload
            yield pkt

    def _name(self, pkt):
        """Generates a name for each template based on the layers of the
        packet."""
        name = 'Template:'
        for l in self._getlayers(pkt):
            name += '/' + l.__class__.__name__
        return name

    @staticmethod
    def _dissect_fields(layer, offset=0):
        """Create the default layer regarding fields_desc dict."""
        diss_fields = OrderedDict()
        start = 0
        p = b""
        flist = []
        for f in layer.fields_desc:
            val = layer.getfieldval(f.name)
            p = f.addfield(layer, p, val)
            if type(p) is tuple or len(p) == 0:
                flist.append(f.name)
            elif start == len(p):
                diss_fields[f.name] = diss_fields[list(diss_fields)[-1]]
            else:
                flist.append(f.name)
                for f in flist:
                    diss_fields[f] = str(
                        slice(start + offset, len(p) + offset))
                flist = []
                start = len(p)
        return diss_fields

    @staticmethod
    def _slices(layer, offset):
        """Get the slice of the fields in the packet."""
        slices = []
        for fname in layer.field_names:
            field = layer.get_field(fname)
            if field.size is not None and int(field.size) > 0 and field.name != '':
                slices.append([field.name,
                               slice(int(field.pos) - offset,
                                     int(field.pos) + int(field.size) - offset)])
        return slices
