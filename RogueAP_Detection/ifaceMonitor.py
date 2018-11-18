#!/usr/bin/python

from scapy.all import *
import pprint
import sys
from time import sleep

def packetAnalyzer(pkt):
	pprint.pprint(pkt)
	print("\n")
	sleep(1)


if __name__== "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ifaceMonitor.py [iface]")
        sys.exit(1)
    
    while True:
		sniff(iface=str(sys.argv[1]), count=1, prn=packetAnalyzer)
		
