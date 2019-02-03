#!/usr/bin/python

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


@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
sio.wait()
