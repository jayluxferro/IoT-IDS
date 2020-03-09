#!/usr/bin/python
"""
IPC
"""

import socketio
import eventlet
import sys
import logger as d
import icmp, syn, udp

# debugging
import pprint

# usage
def usage():
    print('Usage: python {} <interface>'.format(sys.argv[0]))
    sys.exit(1)

## socket defaults
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': '../index.html'}
})

# events
@sio.on('connect')
def connect(sid, environ):
    d.success('Client socket opened => {}'.format(sid))

@sio.on('disconnect')
def disconnect(sid):
    d.error('Client socket closed => {}'.format(sid))


# daemon
if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
