#!/usr/bin/python
"""
ICMP Packet analyzer
Date: 28 Jan 2019
"""
from scapy.all import *
import pprint
import logger as d
import classify as cf
import db

def process(pkt, node, timeSeen):
    ip = pkt.getlayer(IP)
    ether = pkt.getlayer(Ether)
    pprint.pprint(pkt)
    d.default('[+] Time: {}'.format(timeSeen))
    # add to db
    id = db.addData(ether.src, ether.dst, ip.src, ip.dst, timeSeen, node, "", "", "icmp")
    
    # forward data to classify
    cf.classify(pkt, "icmp", node, timeSeen, id)
    
