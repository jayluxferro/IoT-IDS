#!/usr/bin/python
"""
Database Handler
"""

import sqlite3
import sys

sys.path.append('../')
import func
import logger as l

devId = '402e393733393732393635353432'

def init():
    conn = sqlite3.connect("fleet.db")
    conn.row_factory = sqlite3.Row
    return conn


def updateKeys():
    privKey, pubKey = func.genDefaultKeys(1)
    db = init()
    cursor = db.cursor()
    cursor.execute("update keys set privKey=?, pubKey=?, devId=?", (privKey, pubKey, fleetId))
    db.commit()
    l.success("Priv/Pub Keys updated")

def registerDevice(devId, pubKey):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into devices(devId, pubKey, status) values(?, ?, ?)", (devId, pubKey, 0))
    db.commit()
    l.success("IoT Device public key registered")

def getDeviceInfo(devId):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from devices where devId=?", (devId,))
    return cursor.fetchone()


def getDevId():
    return devId
