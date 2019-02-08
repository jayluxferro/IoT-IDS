#!/usr/bin/python

"""
Author: Jay Lux Ferro
Date:  25th Jan 2019
ICMP, SYN and UDP packet analysis
"""

from scapy.all import *
import pprint

icmpFlood = rdpcap("icmp_flood.pcap")
synFlood = rdpcap("syn_flood.pcap")
udpFlood = rdpcap("udp_flood.pcap")
icmpFlood.show()
synFlood.show()
udpFlood[268].psdump("udp_packet")

