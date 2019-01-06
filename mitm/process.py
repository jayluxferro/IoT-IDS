#!/usr/bin/python

import sys
import arp
import db
from scapy.all import *
import time
import json
import yaml
import mitm

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
        #sio.emit('decision', data)
        decide(iface, sio, data, log)
    else:
        # add to arp_cache entry
        log.success('New ARP entry: ' + str(data))
        # sio.emit('add', data)
        log.default('Adding ARP entry: ' + str(data))
        db.add_arp(iface, data)
        arp.add_entry(iface, ip, data['mac'])

def decide(iface, sio, data, log):
    metric = arp.metric(data['ip'])
    if data['res']['ip'] != data['ip']:
        previous_ip = data['res']['ip']
        if previous_ip == '0.0.0.0':
            # capture through EAPOL
            ip = data['ip']
            mac = data['mac']
            seen = data['time']
            db.update_arp(seen, mac, metric)
            arp.add_entry(iface, ip, mac)
        else:
            # not eapol
            mitm.mitm(iface, data) 
            # checking if host is alive
            #arp_packet = ARP(pdst=previous_ip)
            #ans, un = sr(arp_packet)
            #if len(ans.sessions()) >= 1:
                #host is alive
                # mitm detected
               # mitm.mitm(data)
            #else:
                #host not alive; new incoming arp request
                #if int(time.time() - data['res']['last_seen']) >= arp.ttl(iface):
                # new request ; add
                # delete previous ip from db and arp
               # arp.delete_entry(iface, previous_ip)
               # db.delete_entry(previous_ip, data['res']['mac'])
               # arp.add_entry(iface, data['ip'], data['mac'])
    else:
        # update time seen
        seen = data['time']
        mac = data['mac']
        ip = data['ip']
        db.update_arp(seen, mac, metric) 
        arp.update_entry(iface, ip, mac)  
