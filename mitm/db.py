#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date: 29th Dec 2018
Description: MITM Database handler
"""
import sqlite3
import logger as d
import os
import sys
import arp

def init():
    conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) +'/mitm.db')
    conn.row_factory = sqlite3.Row
    return conn

def delete_all(table):
    conn = init()
    conn.cursor().execute('delete from ' + table)
    conn.commit()
    d.success('Deleted virtual ARP cache..')

def find_mac(mac):
    conn = init()
    res = dict()
    data = conn.cursor().execute("select * from arp where mac='" + mac + "'").fetchone()
    if data is not None:
        res['id'] = data['id']
        res['ip'] = str(data['ip'])
        res['mac'] = str(data['mac'])
        res['last_seen'] = data['last_seen']
        res['acq'] = str(data['acq'])
        res['valid'] = data['valid']

    if data is None:
        return False, res
    else:
        return True, res

def add_arp(iface, data):
    conn = init()
    metric = arp.metric(data['ip'])
    conn.cursor().execute('insert into arp(ip, mac, last_seen, acq, valid) values(?, ?, ?, ?, ?)', (data['ip'], data['mac'], data['time'], data['acq'], metric)) 
    conn.commit()
    d.success('Added DB ARP entry => ' + data['ip'] + ' = ' + data['mac'])

def update_arp(seen, mac, metric):
    conn = init()
    conn.cursor().execute("update arp set last_seen='" + str(seen) + "', valid='" + str(metric) + "' where mac='" + mac + "'")
    conn.commit()
    d.success('Updated DB ARP entry => ' + mac ) 

def delete_arp(ip, mac):
    conn = init()
    conn.cursor().execute("delete from arp where ip='" + ip + "' and mac='" + mac + "'")
    conn.commit()
    d.success("Delete DB ARP entry => " + ip + " = " + mac)

def cache():
    conn = init()
    return conn.cursor().execute("select * from arp").fetchall()

def add_detection_time(time):
    conn = init()
    conn.cursor().execute("insert into detections(time) values('" + str(time) + "')")
    conn.commit()

def add_cpu(percent):
    conn = init()
    conn.cursor().execute("insert into cpu(usage) values('" + str(percent) + "')")
    conn.commit()

def add_rtt(time, scenario):
    conn = init()
    conn.cursor().execute("insert into rtt(time, scenario) values('" + str(time) + "', '" + str(scenario) + "')")
    conn.commit()
