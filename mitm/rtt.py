#!/usr/bin/python

import db
import sys
import logger as log
import subprocess

def usage():
    print("Usage: python " + sys.argv[0] + " <ip address> <scenario>")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    ip = sys.argv[1]
    scenario = int(sys.argv[2])

    rtt = subprocess.check_output(['ping', '-c', '1', ip], shell=False).split()[-2].split('/')[0]

    db.add_rtt(rtt, scenario)
    log.success('RTT: ' + str(rtt) + ' ; IP: ' + str(ip))    
