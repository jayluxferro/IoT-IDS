#!/usr/bin/python
"""
SYN packet analyzer
Date: 28th Jan 2019
"""
from scapy.all import *
import pprint

def process(pkt):
    tcp = pkt.getlayer(TCP)
    if tcp.ack != None:
        pprint.pprint(pkt)

