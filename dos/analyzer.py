#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date:   26 Dec 2018
"""

import socketio
from scapy.all import *
import pprint
from time import sleep
import sys
import json
import logger as d
import db
import icmp, syn, udp
import func

sio = socketio.Client()

def packetHandler(pkt):
    global mac
    if pkt.haslayer(IP):
        ip = pkt.getlayer(IP)
        ether = pkt.getlayer(Ether)
        if ip.dst != None and func.inSubnet(ip.dst) and ether.src != mac: # removing data from AP
            if pkt.lastlayer().haslayer(ICMP):
                icmp.process(pkt)

            if pkt.lastlayer().haslayer(UDP):
                udp.process(pkt)

            if pkt.lastlayer().haslayer(TCP):
                syn.process(pkt)

def usage():
    print('Usage: python ' + sys.argv[0] + ' <interface>')

if __name__== '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    ## connecting to rpc via websocket
    sio.connect('http://127.0.0.1:5000')
    #sio.wait()
    
    func.setSubnet(sys.argv[1])
    global mac
    
    mac = db.getSubnet()['mac']

    # sniff for packets
    while True: 
	    sniff(iface=sys.argv[1], count=1, prn=packetHandler)	
