#!/usr/bin/python
"""
SYN packet analyzer
Date: 28th Jan 2019
"""
from scapy.all import *
import pprint
import db

def process(pkt):
    pprint.pprint(pkt)
    tcp = pkt.getlayer(TCP)
    ip = pkt.getlayer(IP)
    ether = pkt.getlayer(Ether)
    db.addP(ether.src, ether.dst, ip.src, ip.dst, tcp.sport, tcp.dport, "tcp")
