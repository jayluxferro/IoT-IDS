#!/usr/bin/python

"""
Functions
"""
import db
import yaml
import sys
sys.path.append('..')
import logger as l

def register(data):
    l.warning(str(data))
    db.registerDevice(data['devId'], data['pubKey'])   

 
