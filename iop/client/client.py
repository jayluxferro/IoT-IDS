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

# Defaults
sio = socketio.Client()
deviceId = func.deviceId()
keys = db.getKeys()

@sio.on('connect')
def on_connect():
    print('connection established')
    sio.emit('online', {'devId': deviceId})
    # register deviceId
    #sio.emit('register', {'devId': deviceId, 'pubKey': keys['pubKey']})

@sio.on(str(deviceId))
def on_message(data):
    print('message received with {0}'.format(data))
    #sio.emit('my response', {'response': 'my response'})

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')
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
