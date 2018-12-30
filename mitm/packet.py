#!/usr/bin/python

"""
Packet Decoder and Encoder
Author: Jay Lux Ferro
Date:   26th Dec 2018
"""
import pprint
import json
import time
from scapy.all import *
import logger as log

def decode(pkt):
    decoded_pkt = []
    
    # EAPOL
    if pkt.haslayer(EAPOL):
        ether_frame = pkt.getlayer(Ether)
        decoded_pkt.append({'ip': '0.0.0.0', 'mac': ether_frame.src, 'time': time.time(), 'acq': 'eapol'})
        decoded_pkt.append({'ip': '0.0.0.0', 'mac': ether_frame.dst, 'time': time.time(), 'acq': 'eapol'}) 

    # DHCP
    if pkt.haslayer(DHCP):
        dhcp_frame = pkt.getlayer(DHCP)
        ether_frame = pkt.getlayer(Ether)

        if dhcp_frame.server_id != None:
            decoded_pkt.append({'ip': dhcp_frame.requested_addr, 'mac': ether_frame.src, 'time': time.time(), 'acq': 'dhcp'})

    # IP
    if pkt.haslayer(IP):
        ip_frame = pkt.getlayer(IP)
        ether_frame = pkt.getlayer(Ether)
        decoded_pkt.append({'ip': ip_frame.src, 'mac': ether_frame.src, 'time': time.time(), 'acq': 'ip'})
        decoded_pkt.append({'ip': ip_frame.dst, 'mac': ether_frame.dst, 'time': time.time(), 'acq': 'ip'})

 
    # ARP
    if pkt.haslayer(ARP):
        arp_frame = pkt.getlayer(ARP)
        decoded_pkt.append({'ip': arp_frame.psrc, 'mac': arp_frame.hwsrc, 'time': time.time(), 'acq': 'arp'})

    log.warning(str(decoded_pkt))       
    return json.dumps(decoded_pkt[0])
