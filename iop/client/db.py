#!/usr/bin/python
"""
Database Handler
"""

import sqlite3
import sys

sys.path.append('../')
import func
import logger as l


def init():
    conn = sqlite3.connect("client.db")
    conn.row_factory = sqlite3.Row
    return conn


def updateKeys():
    privKey, pubKey = func.genDefaultKeys(1)
    db = init()
    cursor = db.cursor()
    cursor.execute("update keys set privKey=?, pubKey=?, devId=?", (privKey, pubKey, func.deviceId()))
    db.commit()
    l.success("Priv/Pub Keys updated")


def addAuth(status, time):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into auth(status, time) values(?, ?)", (status, time))
    db.commit()
    l.default("Added auth data")

def getKeys():
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from keys limit 1")
    return cursor.fetchone()


def addCPU(percent):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into cpu(percent) values(?)", (percent,))
    db.commit()

def getCPU():
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from cpu")
    return cursor.fetchall()

def getRevocation(status):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from auth where status=?", (status,))
    return cursor.fetchall()
