#!/usr/bin/python

import logger as log
import sqlite3
import time

def init():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

def setSubnet(ip, mac):
    db = init()
    cursor = db.cursor()
    cursor.execute("update subnet set ip=?, mac=?", (ip,mac))
    db.commit()
    log.success('Updated subnet')

def getSubnet():
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from subnet limit 1")
    return cursor.fetchone()

def addP(srcMac, dstMac, srcIP, dstIP, sport, dport, category):
    db = init()
    cursor = db.cursor()
    if category == "icmp":
        cursor.execute("insert into icmp(srcMac, dstMac, srcIP, dstIP, time) values(?, ?, ?, ?, ?)", (srcMac, dstMac, srcIP, dstIP, time.time()))
    else:
        # udp and tcp
        cursor.execute("insert into "+ category + "(srcMac, dstMac, srcIP, dstIP, sport, dport, time) values(?, ?, ?, ?, ?, ?, ?)", (srcMac, dstMac, srcIP, dstIP, sport, dport, time.time()))
    db.commit()
    log.default("Added " + category + " Packet details")
    print("\n")


def getP(table):
    con = init()
    cursor = con.cursor()
    cursor.execute("select * from " + str(table) + " order by time")
    return cursor.fetchall()


def updatePInterval(proto, ptime):
    con = init()
    cursor = con.cursor()
    cursor.execute("update config set "+ proto +"=?", (ptime,))
    con.commit()
    log.warning('Updated ' + str(proto) + ' packet interval time')
