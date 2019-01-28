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


def usage():
    print("Usage: python " + str(sys.argv[0]) + " <wlanInterface>")
    sys.exit(1)

def packetHandler(pkt):
    if pkt.haslayer(IP):
        ip = pkt.getlayer(IP)
        if ip.dst != None and func.inSubnet(ip.dst) and ip.src != '60:d8:19:cc:ab:73': # removing data from AP
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

    while True:
        sniff(iface=sys.argv[1], count=1, prn=packetHandler)
