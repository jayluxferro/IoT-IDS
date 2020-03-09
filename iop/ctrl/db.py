#!/usr/bin/python
"""
Database Handler
"""

import sqlite3
import sys

sys.path.append('../')
import func
import logger as l

devId = '502e393733393732393635353432'

def init():
    conn = sqlite3.connect("ctrl.db")
    conn.row_factory = sqlite3.Row
    return conn


def updateKeys():
    privKey, pubKey = func.genDefaultKeys(1)
    db = init()
    cursor = db.cursor()
    cursor.execute("update keys set privKey=?, pubKey=?, devId=?", (privKey, pubKey, devId))
    db.commit()
    l.success("Priv/Pub Keys updated")

def getDevId():
    return devId


def registerDevice(devId, pubKey):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into fleets(fleetId, pubKey, status) values(?, ?, ?)", (devId, pubKey, 0))
    db.commit()
    l.success('Fleet server registered')


def getDeviceInfo(devId):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from fleets where fleetId=?", (devId,))
    return cursor.fetchone()
