#!/usr/bin/python

import sys
import arp
import db
from scapy.all import *
import time
import json
import yaml

def verify(iface, sio, data, log):
    # expecting socket instance and data: ip, mac
    data = yaml.load(data)    
    ip = data['ip']
    mac = data['mac']
    exists, res = db.find_mac(mac)
    data['res'] = res
    if exists is True:
        # send request to decision
        log.warning('Making a decision: ' + str(data))
        sio.emit('decision', data)
    else:
        # add to arp_cache entry
        log.success('New ARP entry: ' + str(data))
        sio.emit('add', data)


def decide(iface, sio, data, log):
    if data['res']['ip'] != data['ip']:
        previous_ip = data['res']['ip']
        # checking if host is alive
        arp_packet = ARP(pdst=previous_ip)
        ans, un = sr(arp_packet)
        if len(ans.sessions()) >= 1:
            #host is alive
            # mitm detected
            sio.emit('mitm', data)
        else:
            #host not alive; new incoming arp request
            #if int(time.time() - data['res']['last_seen']) >= arp.ttl(iface):
                # new request ; add
            arp.add_entry(iface, data['ip'], data['mac'])
