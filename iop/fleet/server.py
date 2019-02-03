#!/usr/bin/python

"""
Fleet Server
"""

import socketio
import eventlet
import sys

sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf8')
import logger as l

# Socket defaults
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': '../index.html'}
})


# event handlers
@sio.on('connect')
def connect(sid, environ):
    l.default('Client socket opened => {0}'.format(str(sid)))


@sio.on('disconnect')
def disconnect(sid):
    l.error('Client socket closed => {0}'.format(str(sid)))


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
