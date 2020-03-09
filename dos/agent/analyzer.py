#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date:   9th February, 2020
Task:   Packet analyzer for DoS
"""

import sys
import logger as d
from scapy.all import *
import socketio
import func
import db
import time
import icmp, udp, syn
import netfilter as nf

# debugging
import pprint

# inits
sio = socketio.Client()
server='http://127.0.0.1:5000'
icmp_pkt_arr = 0
udp_pkt_arr = 0
tcp_pkt_arr = 0

def usage():
    print('Usage: python {} <interface> <node>'.format(sys.argv[0]))
    sys.exit(1)

# packet handler
def packetHandler(pkt):
    global mac
    global icmp_pkt_arr
    global udp_pkt_arr
    global tcp_pkt_arr
    global node
    pprint.pprint(pkt)

    if pkt.haslayer(IP):
        ip = pkt.getlayer(IP)
        ether = pkt.getlayer(Ether)
        if ip.dst != None and func.inSubnet(ip.dst) and ether.src != mac: # removing data from AP
            if pkt.lastlayer().haslayer(ICMP):
                if icmp_pkt_arr == 0:
                    icmp_pkt_arr = time.time()
                else:
                    timeSeen = time.time()
                    if timeSeen - icmp_pkt_arr <= func.tau():
                        d.warning('[+] Possible ICMP Flood detected')
                        icmp_pkt_arr = timeSeen
                        icmp.process(pkt, node, timeSeen)
                    else:
                        # reset
                        d.default('[-] Resetting icmp_pkt_arr')
                        icmp_pkt_arr = 0
            if pkt.lastlayer().haslayer(UDP):
                if udp_pkt_arr == 0:
                    udp_pkt_arr = time.time()
                else:
                    timeSeen = time.time()
                    if timeSeen - udp_pkt_arr <= func.tau():
                        d.warning('[+] Possible UDP Flood detected')
                        udp_pkt_arr = timeSeen
                        udp.process(pkt, node, timeSeen)
                    else:
                        # reset
                        d.default('[-] Resetting udp_pkt_arr')
                        udp_pkt_arr = 0

            if pkt.lastlayer().haslayer(TCP):
                if tcp_pkt_arr == 0:
                    tcp_pkt_arr = time.time()
                else:
                    timeSeen = time.time()
                    if timeSeen - tcp_pkt_arr <= func.tau():
                        d.warning('[+] Possible TCP Flood detected')
                        tcp_pkt_arr = timeSeen
                        syn.process(pkt, node, timeSeen)
                    else:
                        # reset
                        d.default('[-] Resetting tcp_pkt_arr')
                        tcp_pkt_arr = 0

# entry
if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()

    # connect to rpc
    sio.connect(server)
    
    func.setSubnet(sys.argv[1])
    global mac
    global node
    node = sys.argv[2]
    mac = db.getSubnet()['mac']
    nf.reset()

    # sniff for packets
    while True:
        sniff(iface=sys.argv[1], count=1, prn=packetHandler)
