#!/usr/bin/python
"""
NetFilter
"""

import logger as d
import pprint
import subprocess
import db
import time
from scapy.all import *

def filter(pkt, proto, node, timeSeen, id):
    pprint.pprint(pkt)
    d.error('[+] Defending: {}'.format(proto))

    if proto == "icmp":
        # iptables -A OUTPUT -p icmp --icmp-type echo-request -j DROP
        # iptables -I INPUT -p ICMP -j DROP
        #subprocess.check_call(['iptables','-A', 'OUTPUT', '-p', 'icmp', '--icmp-type', 'echo-request', '-j', 'DROP'])
        subprocess.check_call(['iptables', '-A', 'INPUT', '-p', 'icmp', '-j', 'DROP'])
        subprocess.check_call(['./blockICMP'])
    else:
        if proto == "udp":
            stack = pkt.getlayer(UDP)
        else:
            stack = pkt.getlayer(TCP)
        print(stack.dport, proto)
        # iptables -A INPUT -p udp dport 5050 -j DROP
        #subprocess.check_call(['iptables', '-A', 'INPUT', '-p', proto, 'dport', stack.dport, '-j', 'DROP'])
        subprocess.check_call(['./blockTCP_UDP', str(proto), str(stack.dport)])
    # log data
    db.addDefense(node, proto, time.time() - timeSeen)

def reset():
    d.default('[+] Resetting ')
    subprocess.check_call(['iptables', '-F'])
    subprocess.check_call(['iptables', '-X'])
    subprocess.check_call(['iptables', '-t','nat', '-F'])
    subprocess.check_call(['iptables', '-t', 'nat', '-X'])
    subprocess.check_call(['iptables', '-t', 'mangle', '-F'])
    subprocess.check_call(['iptables', '-t', 'mangle', '-X'])
    subprocess.check_call(['iptables', '-P', 'INPUT', 'ACCEPT'])
    subprocess.check_call(['iptables', '-P', 'FORWARD', 'ACCEPT'])
    subprocess.check_call(['iptables', '-P', 'OUTPUT', 'ACCEPT'])
