#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date:   7th January, 2019
Packet Analysis
EAPOL, 
"""
import sys
from scapy.all import *
import pprint

eapol = False
dhcp = False
ip = False
arp = False

def usage():
    print("Usage: python " + sys.argv[0] + " <pcap file>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    pkt = rdpcap(sys.argv[1])
    print(pkt.nsummary())
   
    pkt[0].psdump('arp')
    pkt[10].psdump('arp2')
    pkt[4].psdump('eapol')
    pkt[4].psdump('eapol2')
    pkt[63].psdump('dhcp')
    pkt[78].psdump('ip')

     
