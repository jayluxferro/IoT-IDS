#!/usr/bin/python
"""
Author: Jay Lux Ferro
Date:   26 Dec 2018
Detection engine
"""

import socketio
from scapy.all import *
import pprint
from time import sleep
import sys
import json
import logger as d
import db
import func

sio = socketio.Client()

###### events ######
@sio.on('udp_p')
def udp(sid, data):
    d.default(data)

@sio.on('tcp_p')
def tcp(sid, data):
    d.default(data)

@sio.on('icmp_p')
def icmp(sid, data):
    d.default(data)

####################

def usage():
    print('Usage: python ' + sys.argv[0] + ' <interface>')

if __name__== '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    ## connecting to rpc via websocket
    sio.connect('http://127.0.0.1:5000')
    sio.wait()
   
    
