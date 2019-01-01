#!/usr/bin/python

"""
Author: Jay Lux Ferro
Date: 1 Jan 2019
Description: MITM Handler
"""
import db
import logger as log
from scapy.all import *
import arp

def mitm(iface, data):
    log.default('Detecting MITM => ' + str(data['ip']) + ' = ' + str(data['mac']))
    db_data = data['res']
    i_data_ip = data['ip']
    i_data_mac = data['mac']
    i_data_acq = data['acq']
    i_data_metric = data['valid']
    i_data_time = data['time']

    db_data_ip = db_data['ip']
    db_data_mac = db_data['mac']
    db_data_acq = db_data['acq']
    db_data_metric = db_data['valid']
    db_data_time = db_data['last_seen']

    # both macs are the same
    exists, i_db_data = db.find_mac(i_data_mac) # asset exists is true
    
    # checking if host previous_ip is up
    arp_packet = ARP(pdst=db_data_ip)
    ans, un = sr(arp_packet)
    if len(ans.sessions()) >= 1:
        # host is alive
        log.error('MITM Detected => IP: ' + i_db_data['ip'] + ', MAC: ' + i_db_data['mac'] + ' ::: Spoofing Client ::: IP: ' + i_data_ip + ', MAC: ' + db_data_mac)
        # add mitigation
        # delete incoming arp entry and keep new one
        arp.delete_entry(iface, i_data_ip, i_data_mac)
        arp.add_entry(iface, db_data_ip, db_data_mac)
    else:
        # possible DOS;
        metric = arp.metric(db_data_ip)
        if metric != 1:
            # authorized client has been blocked
            # checking last time seen
            if (i_data_time - db_data_time) < arp.ttl(iface):
                # confirmed dos
                arp_delete(iface, i_data_ip, i_data_mac)
                 
                log.error('MITM Detected => IP: ' + i_db_data['ip'] + ', MAC: ' + i_db_data['mac'] + ' ::: Spoofing Client ::: IP: ' + i_data_ip + ', MAC: ' + db_data_mac)
     
