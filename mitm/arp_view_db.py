#!/usr/bin/python

import sys
from time import sleep
import subprocess
import db

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
        for x in db.cache():
            print("|\t" + str(x['ip']) + "\t|\t" + str(x['mac']) + "  |")

        lines()
        sleep(5)
