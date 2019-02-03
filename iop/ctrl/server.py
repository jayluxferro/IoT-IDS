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
import db

# Socket defaults
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': '../index.html'}
})


# event handlers
@sio.on('connect')
def connect(sid, environ):
    l.default('Client socket opened => {0}'.format(str(sid)))


@sio.on('register')
def register(sid, data):
    fx.register(data)    

@sio.on('online')
def online(sid, data):
    l.success(str(data))
    devInfo = db.getDeviceInfo(data['devId'])
    if devInfo['status'] == 0:
        sio.disconnect(sid)
        return
    l.default('Fleet: {0} is online'.format(data['devId']))

@sio.on('disconnect')
def disconnect(sid):
    l.error('Client socket closed => {0}'.format(str(sid)))


@sio.on('auth')
def auth(sid, data):
    l.default('Sending request to fleet server')
    sio.emit(str(data['fleetId']), data)

if __name__ == "__main__":
    #db.updateKeys()
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 6000)), app)
