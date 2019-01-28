#!/usr/bin/python
"""
ICMP Packet analyzer
Date: 28 Jan 2019
"""
from scapy.all import *
import pprint

def process(pkt):
    pprint.pprint(pkt) 
