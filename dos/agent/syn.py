#!/usr/bin/python
"""
SYN packet analyzer
Date: 28th Jan 2019
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
    stack = pkt.getlayer(TCP)
    d.default('[+] Time: {}'.format(timeSeen))
    # add to db
    id = db.addData(ether.src, ether.dst, ip.src, ip.dst, timeSeen, node, stack.sport, stack.dport, "tcp")
    
    # forward data to classify
    cf.classify(pkt, "tcp", node, timeSeen, id)
    
