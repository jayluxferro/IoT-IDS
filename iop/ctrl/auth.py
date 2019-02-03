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

@sio.on('connect')
def on_connect():
    print('connection established')
    sio.emit('auth', {'fleetId': sys.argv[1], 'devId': sys.argv[2], 'status': int(sys.argv[3])})
    #sio.disconnect()

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')


def initialize():
    try:
        sio.connect('http://localhost:6000')
        sio.wait()
    except:
        l.error('Failed to connect to ctrl server')
        sleep(5)
        initialize()


def usage():
    print("Usage: python {0} <fleetId> <devId> <status>".format(str(sys.argv[0])))
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        
    initialize()
