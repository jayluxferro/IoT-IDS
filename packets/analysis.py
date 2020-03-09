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

def packetHandler(pkt):
    global eapol
    global dhcp
    global ip
    global arp
 
    # EAPOL
    if pkt.haslayer(EAPOL) and eapol is False:
        pkt.getlayer(EAPOL).psdump('eapol')
        eapol = True

    # DHCP
    if pkt.haslayer(DHCP) and dhcp is False:
        pkt.getlayer(DHCP).psdump('dhcp')
        dhcp = True

    # IP
    if pkt.haslayer(IP) and ip is False:
        pkt.getlayer(IP).psdump('ip')
        ip = True

    # ARP
    if pkt.haslayer(ARP) and arp is False:
       pkt.getlayer(ARP).psdump('arp')
       arp = True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    sniff(offline=sys.argv[1], prn=packetHandler)
