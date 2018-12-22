#!/usr/bin/python
# Detecting arspoofing traffic

from scapy.all import *
import pprint
from time import sleep
import sys

def packetAnalyzer(pkt):
	pprint.pprint(pkt)
    

def usage():
    print("Usage: python "+ sys.argv[0] + " wlan0")

if __name__== "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    while True:
    	sniff(filter="arp", iface=sys.argv[1], prn=packetAnalyzer)
		
