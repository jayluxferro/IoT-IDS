#!/usr/bin/python
<<<<<<< HEAD
# Detecting arspoofing traffic
=======
>>>>>>> 4b342e43838d8a108d0fdef15faa78873ec7e970

from scapy.all import *
import pprint
from time import sleep
import sys

def packetAnalyzer(pkt):
	pprint.pprint(pkt)
<<<<<<< HEAD
    
=======
	print("\n")
	sleep(1)
>>>>>>> 4b342e43838d8a108d0fdef15faa78873ec7e970

def usage():
    print("Usage: python "+ sys.argv[0] + " wlan0")

if __name__== "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
<<<<<<< HEAD
    while True:
    	sniff(filter="arp", iface=sys.argv[1], prn=packetAnalyzer)
=======

    while True:
		sniff(iface=sys.argv[1], count=1, prn=packetAnalyzer)
>>>>>>> 4b342e43838d8a108d0fdef15faa78873ec7e970
		
