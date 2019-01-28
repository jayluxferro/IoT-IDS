#!/usr/bin/python
"""
Functions
"""
import subprocess
import logger as log
import db

def inSubnet(ip):
    subnet = db.getSubnet().encode('utf-8')
    # classful
    subnet = subnet.split('/')
    c = subnet[-1]
    r = int(int(c)/8)
    ip = ip.split('.')
    subnet = subnet[0].split('.')
    if subnet[:r] == ip[:r]:
        return True
    return False

def setSubnet(iface):
    gw = subprocess.check_output(['ip','addr','show',iface], shell=False)
    gw = gw.splitlines()[2].split(' ')[5]
    db.setSubnet(gw)   

