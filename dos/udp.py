#!/usr/bin/python
"""
UDP Packet Analyzer
Date: 28th Jan 2019
"""

from scapy.all import *
import pprint
import db

def process(pkt, scenario):
    pprint.pprint(pkt)
    ip = pkt.getlayer(IP)
    ether = pkt.getlayer(Ether)
    udp = pkt.getlayer(UDP)
    db.addP(ether.src, ether.dst, ip.src, ip.dst, udp.sport, udp.dport, "udp", scenario) 
