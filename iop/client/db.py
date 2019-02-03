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
