#!/usr/bin/python
"""
Time decomposition test
Date: 28th Jan 2019
Author: Jay Lux Ferro
"""

from scapy.all import *
import pprint
import time
import logger as log
import icmp, syn, udp
import func
import sys
import db


def usage():
    print("Usage: python " + str(sys.argv[0]) + " <wlanInterface>")
    sys.exit(1)

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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    func.setSubnet(sys.argv[1])
    global mac
    
    mac = db.getSubnet()['mac']

    while True:
        sniff(iface=sys.argv[1], count=1, prn=packetHandler)
