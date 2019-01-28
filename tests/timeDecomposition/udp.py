#!/usr/bin/python
"""
UDP Packet Analyzer
Date: 28th Jan 2019
"""

from scapy.all import *
import pprint

def process(pkt):
    pprint.pprint(pkt)
