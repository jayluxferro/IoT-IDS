#!/usr/bin/python
"""
CPU Data
"""

import func
import db
from time import sleep
import sys

def usage():
    print("python {} <node> <scenario - 0, 1>".format(sys.argv[0]))
    sys.exit(1)

if __name__=="__main__":
    if len(sys.argv) != 3:
        usage()

    node = sys.argv[1]
    scenario = sys.argv[2]

    for i in range(20):
        db.addCPU(node, scenario, func.cpu_percent(), func.memory()[2])
        sleep(5)
