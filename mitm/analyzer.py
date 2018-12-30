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

sio = socketio.Client()

def packetAnalyzer(pkt):
    # sending decoded packet info to detection bridge
    sio.emit('detect', packet.decode(pkt))

def usage():
    print('Usage: python ' + sys.argv[0] + ' <interface>')

if __name__== '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    ## connecting to rpc via websocket
    sio.connect('http://127.0.0.1:5000')
    #sio.wait()
    
    ## Delete arp cache entries
    sio.emit('delete', None)
    db.delete_all('arp')

    # sniff for ARP packets
    while True: 
	    sniff(filter='arp', iface=sys.argv[1], count=1, prn=packetAnalyzer)	
