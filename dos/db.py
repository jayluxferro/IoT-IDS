#!/usr/bin/python

import logger as log
import sqlite3
import time
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

def addCPU(node):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into cpu(usage, node) values(?, ?)", (func.cpu_percent(), node))
    db.commit()

def addP(srcMac, dstMac, srcIP, dstIP, sport, dport, category, scenario, node, psize):
    db = init()
    cursor = db.cursor()
    additionalParams = list(func.getAdditionalParams())
    if category == "icmp":
        params = [srcMac, dstMac, srcIP, dstIP, time.time(), scenario, node, psize]
        
        for _ in additionalParams: params.append(_)

        cursor.execute("insert into icmp(srcMac, dstMac, srcIP, dstIP, time, scenario, node, psize, freq_c, freq_min, freq_max, cpu_percent, ctx_switches, interrupts, soft_interrupts, syscalls, mtu, battery, fan, temp_c, temp_h, temp_crit, swap_t, swap_u, swap_f, swap_p, mem_t, mem_a, mem_p, mem_u, mem_f) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(params))
    else:
        # udp and tcp
        params = [srcMac, dstMac, srcIP, dstIP, sport, dport, time.time(), scenario, node, psize]
        for _ in additionalParams: params.append(_)

        cursor.execute("insert into "+ category + "(srcMac, dstMac, srcIP, dstIP, sport, dport, time, scenario, node, psize, freq_c, freq_min, freq_max, cpu_percent, ctx_switches, interrupts, soft_interrupts, syscalls, mtu, battery, fan, temp_c, temp_h, temp_crit, swap_t, swap_u, swap_f, swap_p, mem_t, mem_a, mem_p, mem_u, mem_f) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(params))
    db.commit()
    log.default("Added " + category + " Packet details")
    print("\n")


def getP(table):
    con = init()
    cursor = con.cursor()
    cursor.execute("select * from " + str(table) + " order by time")
    return cursor.fetchall()


def getPS(table, scenario):
    con = init()
    cursor = con.cursor()
    cursor.execute("select * from " + str(table) + " where scenario=? order by time", (scenario,))
    return cursor.fetchall()

def config():
    con = init()
    cursor = con.cursor()
    cursor.execute("select * from config limit 1")
    return cursor.fetchone()

def updatePInterval(proto, ptime):
    con = init()
    cursor = con.cursor()
    cursor.execute("update config set "+ proto +"=?", (ptime,))
    con.commit()

