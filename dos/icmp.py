#!/usr/bin/python
"""
ICMP Packet analyzer
Date: 28 Jan 2019
"""
from scapy.all import *
import pprint
import db

def process(pkt, scenario, node):
    pprint.pprint(pkt) 
    ip = pkt.getlayer(IP)
    ether = pkt.getlayer(Ether)
    db.addP(ether.src, ether.dst, ip.src, ip.dst, "", "", "icmp", scenario, node, len(pkt))

def detect():
    pass
