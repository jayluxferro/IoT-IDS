#!/usr/bin/python3

from scapy.all import *
import pprint
from time import sleep

def packetAnalyzer(pkt):
	pprint.pprint(pkt)
	print("\n")
	sleep(1)


if __name__== "__main__":
	while True:
		sniff(iface='eth0', count=1, prn=packetAnalyzer)
		
