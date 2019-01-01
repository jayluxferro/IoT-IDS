#!/usr/bin/python
"""
ARP cache data
Author: Jay Lux Ferro
Date:   26 Dec 2018
"""

import sys
import os
import db
import subprocess
import logger as log

def cache(iface):
    result = subprocess.check_output(['arp', '-a', '-i', iface], shell=False).split('\n')
    arp_data = []
    for x in result:
        fields = x.split(' ')
        if len(fields) is not 7:
            continue
        ip_address = fields[1].strip('()')
        mac_address = fields[3]
        interface = fields[6]
        gateway = True if fields[0] == '_gateway' else False
        
        # append data
        if ip_address != 'in':
            arp_data.append({'ip': ip_address, 'mac': mac_address, 'interface': interface, 'gateway': gateway})
    return arp_data
   
def ttl(iface):
    return int(subprocess.check_output(['cat', '/proc/sys/net/ipv4/neigh/' + iface + '/gc_stale_time'], shell=False).strip())

def delete_all_entries(iface):
    arp_data = cache(iface)
    for x in arp_data:
        delete_entry(iface, x['ip'])

def delete_entry(iface, ip):
    res = subprocess.check_output(['arp', '-i', iface, '-d', ip], shell=False) 

def find(iface, ip, mac):
    exists = False
    res = None
    for x in cache(iface):
         if x['mac'] == mac:
            exits = True
            res = x
    return exists, res

def find_mac(iface, ip, mac):
    return db.find_mac(mac)

def add_entry(iface, ip, mac):
    iface = str(iface)
    ip = str(ip)
    mac = str(mac)
    if ip != '0.0.0.0':
        res = subprocess.check_output(['arp', '-i', iface, '-s', ip, mac], shell=False)
        log.success('Added Sys ARP Entry => ' + ip + ' = ' + mac)
        
def update_entry(iface, ip, mac):
    delete_entry(iface, ip)
    add_entry(iface, ip, mac)

def metric(ip):
    result = subprocess.check_output(['traceroute', '--max-hops=1', ip], shell=False)
    result = tuple(result.split('\n')[1])
    counter = 0
    for x in result:
        if(x == '*'):
            counter += 1
    
    if counter >= 1:
        return 1
    else:
        return 2
