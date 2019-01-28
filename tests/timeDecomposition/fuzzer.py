#!/usr/bin/python
# tcp fuzzer; spoofing mac

from scapy.all import *

pkt = Ether(dst='c4:e9:84:df:3c:98', src='00:11:22:33:44:55')/IP(version=4, src='8.8.8.8', dst='172.24.1.1')/TCP(sport='http', dport=80)

sendp(pkt, iface='wlan0')
