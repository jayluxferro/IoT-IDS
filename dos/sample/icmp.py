#!/usr/bin/python

'''
Author: Jay Lux Ferro
Date:  25th Jan 2019
ICMP packet analysis
'''

from scapy.all import *
import pprint

icmpFlood = rdpcap('icmp_flood2.pcap')

# icmpFlood.show()
for x in range(100, 110):
    pprint.pprint(icmpFlood[x])

icmpFlood[100].psdump('icmp_packet')