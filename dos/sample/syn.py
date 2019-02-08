#!/usr/bin/python

'''
Author: Jay Lux Ferro
Date:  25th Jan 2019
ICMP, SYN and UDP packet analysis
'''

from scapy.all import *
import pprint

from scapy.all import *
import pprint

synFlood = rdpcap('syn_flood2.pcap')


for x in range(100, 110):
    pprint.pprint(synFlood[x])
    print('\n')


# dumping only one format
synFlood[100].psdump('syn_packet')

