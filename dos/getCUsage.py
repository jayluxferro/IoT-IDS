import db
from time import sleep
import sys

def usage():
    print("Usage: python {} <node>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 2:
    usage()


node = sys.argv[1]

for _ in range(100):
    db.addCPU(node)
    sleep(1)
