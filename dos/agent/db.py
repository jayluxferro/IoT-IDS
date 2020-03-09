#!/usr/bin/python

import logger as log
import sqlite3
import func 

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


def addData(dstMac, dstIP, srcMac, srcIP, timeSeen, node, sport, dport, proto):
    db = init()
    cursor = db.cursor()
    cpu_percent = func.cpu_percent()
    mem_p = func.memory()[2]
    cursor.execute("insert into data(dstMac, dstIP, srcMac, srcIP, time, node, sport, dport, proto, cpu_percent, mem_p) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dstMac, dstIP, srcMac, srcIP, timeSeen, node, sport, dport, proto, cpu_percent, mem_p))
    db.commit()
    log.default('[-] {} data added'.format(proto))
    return cursor.lastrowid

def getCData(currentTime, proto, node):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from data where proto=? and node=? and " + str(currentTime) + " - time <= " + str(func.tau()), (proto, node))
    return cursor.fetchall()

def addDetection(node, proto, dTime):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into detection(node, proto, time) values(?, ?, ?)", (node, proto, dTime))
    db.commit()
    log.success('[+] DoS Detection data logged')

def addDefense(node, proto, dTime):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into defense(node, proto, time) values(?, ?, ?)", (node, proto, dTime))
    db.commit()
    log.success('[+] DoS Defense data logged')

def addCPU(node, scenario, cpu, mem):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into cpu(node, scenario, cpu, mem) values(?, ?, ?, ?)", (node, scenario, cpu, mem))
    db.commit()
    log.success('[+] CPU data added: Node => {}, Scenario => {}'.format(node, scenario))

def getTable(tableName):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from " + str(tableName))
    return cursor.fetchall()
