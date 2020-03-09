#!/usr/bin/python

"""
Author: Jay Lux Ferro
Date:  25th Jan 2019
ICMP, SYN and UDP packet analysis
"""

from scapy.all import *
import pprint


from scapy.all import *
import pprint

udpFlood = rdpcap('udp_flood2.pcap')


for x in range(100, 110):
    pprint.pprint(udpFlood[x])
    print('\n')


udpFlood[100].psdump('udp_packet')


