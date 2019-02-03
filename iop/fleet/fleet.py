#!/usr/bin/python
"""
Fleet Client
"""

import sys
sys.path.append('..')
import func
import logger as l
import db
import socketio
reload(sys)
sys.setdefaultencoding('utf8')
import fx

# Defaults
sio = socketio.Client()
devInfo = db.getDeviceInfo(db.getDevId())

@sio.on('connect')
def on_connect():
    l.success('connection established')
    # register deviceId
    #sio.emit('register', {'devId': db.getDevId(), 'pubKey': devInfo['pubKey']})
    sio.emit('online', {'devId': db.getDevId()})

@sio.on(str(db.getDevId()))
def on_message(data):
    l.default('message received with {0}'.format(str(data)))
    fx.sendDeviceMessage(str(data['fleetId']), data)
    #sio.emit('my response', {'response': 'my response'})

@sio.on('disconnect')
def on_disconnect():
    l.error('disconnected from server')


try:
    sio.connect('http://localhost:6000')
    sio.wait()
except:
    l.error('Failed to connect to ctrl server')
    sys.exit(0)
