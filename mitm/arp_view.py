#!/usr/bin/python

import arp
import sys
from time import sleep
import subprocess

def lines():
    print("*" * 52)

def usage():
    print("Usage: python " + sys.argv[0] + " <interface>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    while True:
        res = subprocess.call(['clear'])
        lines()
        print("|\t IP Address\t|  \t MAC Address \t  |")
        lines()
        for x in arp.cache(sys.argv[1]):
            print("|\t" + str(x['ip']) + "\t|\t" + str(x['mac']) + "  |")

        lines()
        sleep(5)
