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
    return sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) +'/mitm.db')

def delete_all(table):
    conn = init()
    conn.cursor().execute('delete from ' + table)
    conn.commit()
    d.success('Deleted virtual ARP cache..')

def find_mac(mac):
    conn = init()
    res = conn.cursor().execute("select * from arp where mac='" + mac + "'").fetchone()
    if res == None:
        return False, res
    else:
        return True, res

def add_arp(iface, data):
    conn = init()
    conn.cursor().execute('insert into arp(ip, mac, last_seen, acq, valid) values(?, ?, ?, ?, ?)', (data['ip'], data['mac'], data['time'], data['acq'], 1)) 
    conn.commit()
    arp.update_entry(iface, data['ip'], data['mac'])    
    d.success('Added ARP entry => ' + data['ip'] + ' = ' + data['mac'])
