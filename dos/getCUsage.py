import db
from time import sleep
import sys

def usage():
    print("Usage: python {} <node>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 2:
    usage()


node = sys.argv[1]
for scenario in range(1, 4): # scenario
    print("Scenario {}".format(scenario))
    for _ in range(300):
        db.addCPU(node, scenario)
        sleep(1)

    sleep(30)
