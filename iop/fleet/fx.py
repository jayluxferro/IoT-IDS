#!/usr/bin/python

"""
Functions
"""
import db
import yaml
import sys
sys.path.append('..')
import logger as l
import socketio

# Defaults
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    global devId
    global data
    l.default('Sending request to IoT device')
    sio.emit(devId, data)
    #sio.disconnect()

def register(data):
    l.warning(str(data))
    db.registerDevice(data['devId'], data['pubKey'])   

def sendDeviceMessage(d, message):
    global devId
    global data
    devId = d
    data = message
    try:
        sio.connect('http://localhost:5000')
    except:
        l.error('Failed to connect to ctrl server')
        sys.exit(0)
