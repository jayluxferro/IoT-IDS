#!/usr/bin/python
"""
Device Client
"""
from time import sleep
import sys
sys.path.append('..')
import func
import logger as l
import db
import socketio
reload(sys)
sys.setdefaultencoding('utf8')
from binascii import hexlify, unhexlify
import time


# Defaults
sio = socketio.Client()
deviceId = func.deviceId()
keys = db.getKeys()

@sio.on('connect')
def on_connect():
    l.success('connection established')
    sio.emit('online', {'devId': deviceId})
    # register deviceId
    #sio.emit('register', {'devId': deviceId, 'pubKey': keys['pubKey']})

@sio.on(str(deviceId))
def on_message(data):
    keys = db.getKeys()
    data['status'] = func.decrypt(keys['privKey'], unhexlify(data['status']))
    data['time'] = func.decrypt(keys['privKey'], unhexlify(data['time']))
    #sio.emit('my response', {'response': 'my response'})
    db.addAuth(data['status'], float(time.time() - float(data['time'])))
    l.warning('message received with {0}'.format(data))

@sio.on('disconnect')
def on_disconnect():
    l.error('disconnected from server')
    sio.emit('offline', {'deviceId': deviceId})
    initialize()


def initialize():
    try:
        sio.connect('http://localhost:5000')
        sio.wait()
    except:
        l.error('Failed to connect to fleet server')
        sleep(5)
        initialize()

initialize()
