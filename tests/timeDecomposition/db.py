#!/usr/bin/python

import logger as log
import sqlite3


def init():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

def setSubnet(ip):
    db = init()
    cursor = db.cursor()
    cursor.execute("update subnet set ip=?", (ip,))
    db.commit()
    log.success('Updated subnet')

def getSubnet():
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from subnet limit 1")
    return cursor.fetchone()['ip']

