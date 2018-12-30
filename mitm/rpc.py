#!/usr/bin/python
"""
RPC server
Author: Jay Lux Ferro
Date:   26 Dec 2018
"""

import socketio
import eventlet
import pprint
import packet, arp
import sys
import logger as d
import db
######################### DEFAULTS ##############################
# usage
def usage():
    print('Usage: python ' + sys.argv[0] + ' <interface>')

## Socket defaults
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

#### Connection Defaults
@sio.on('connect')
def connect(sid, environ):
    d.success('Client socket opened => '+ sid)

@sio.on('disconnect')
def disconnect(sid):
    d.error('Client socket closed => '+ sid)

#### Sending decoded Inforation to detection bridge
@sio.on('detect')
def analyze_packet(sid, data):
    d.default('Verifying ' + str(data))
    sio.emit('verify', data)   

### Delete all arp entries
@sio.on('delete')
def delete_arp_entries(sid):
    d.warning('Deleting arp cache entries..')
    arp.delete_all_entries(sys.argv[1])
##################################################################



#### Websocket daemon
if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

        sys.exit()
    
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)

