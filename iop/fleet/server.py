#!/usr/bin/python

"""
Fleet Server
"""

import socketio
import eventlet
import sys
import db

sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf8')
import logger as l
import fx
from binascii import hexlify, unhexlify
import func


# Socket defaults
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': '../index.html'}
})


# event handlers
@sio.on('connect')
def connect(sid, environ):
    l.default('Client socket opened => {0}'.format(str(sid)))


@sio.on('online')
def online(sid, data):
    l.success(str(data))
    devInfo = db.getDeviceInfo(data['devId'])
    if devInfo['status'] == 0:
        sio.disconnect(sid)
        return
    l.default('Device: {0} is online'.format(data['devId']))

@sio.on('disconnect')
def disconnect(sid):
    l.error('Client socket closed => {0}'.format(str(sid)))


@sio.on('register')
def register(sid, data):
    fx.register(data)    


@sio.on('offline')
def offline(sid, data):
    l.warning('Client {0} is offline'.format(str(sid)))



@sio.on(str(db.getDevId()))
def auth(sid, data):
    # decrypting data
    keys = db.getKeys()
    data['status'] = func.decrypt(keys['privKey'], unhexlify(data['status']))
    data['time'] = func.decrypt(keys['privKey'], unhexlify(data['time']))
    
    # update status
    db.updateStatus(data['devId'], data['status'])

    # encrypting data
    deviceInfo = db.getDeviceInfo(str(data['devId']))
    data['status'] = hexlify(func.encrypt(str(deviceInfo['pubKey']), data['status']))
    data['time'] = hexlify(func.encrypt(str(deviceInfo['pubKey']), data['time']))
     
          
    sio.emit(str(data['devId']), data)

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
    #db.updateKeys()
