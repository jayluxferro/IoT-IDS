#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date:   26 Dec 2018
"""

import socketio
from scapy.all import sniff
import pprint
from time import sleep
import sys
import json
import packet
import logger as d
import db
import process

sio = socketio.Client()

####################### DETECTION ################################
@sio.on('verify')
def verify_arp(data):
    d.default('Processing verification: ' + str(data))
    process.verify(sys.argv[1], sio, data, d)

@sio.on('add')
def add_arp(data):
    d.default('Adding ARP entry: ' + str(data))
    db.add_arp(sys.argv[1], data)

@sio.on('decision')
def arp_decision(data):
    d.default('Making ARP decision: ' + str(data))
    process.decide(sys.argv[1], sio, data, d)
##################################################################

def usage():
    print('Usage: python ' + sys.argv[0] + ' <interface>')

if __name__== '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    ## connecting to rpc via websocket
    sio.connect('http://127.0.0.1:5000')
    #sio.wait()
    
