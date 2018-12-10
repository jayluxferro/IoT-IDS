#!/usr/bin/python

import psutil
import db
import os

def get_usage():
    pid = os.getpid()
    py = psutil.Process(pid)
    return py.memory_percent()

def getCollisionsAvg(table, start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select avg(collisions) from " + table + " where counter >=? and counter <=? and scenario=?", (start, stop, scenario)).fetchone()[0]

def getCollisionsSum(table, start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select sum(collisions) from "+ table + " where counter >=? and counter <=? and scenario = ?", (start, stop, scenario)).fetchone()[0]

def getHwCollision(table, start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select sum(collisions) from "+ table + " where counter >= ? and counter <= ? and scenario = ?", (start, stop, scenario)).fetchone()[0]

def getAvg(field, table, start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select avg("+ field + ") from "+ table + " where counter >= ? and counter <= ? and scenario = ?", (start, stop, scenario)).fetchone()[0]


def mod(x, y):
    return x % y

def wh64(s1, s2, s3, m):
    s1 = mod(171 * s1, 30269)
    s2 = mod(172 * s2, 30307)
    s3 = mod(170 * s3, 30323)
    r = mod(s1/30269.0 + s2/30307.0 + s3/30323.0, float(m))
    return r, s1, s2, s3

def wh16(s1, s2, s3, m):
    s1 = 171 * mod(s1, 177) - 2 * (s1 / 177)
    s2 = 172 * mod(s2, 176) - 35 * (s2 / 176)
    s3 = 170 * mod(s3, 178) - 63 * (s3 / 178)
    r = mod((s1/30269.0 + s2/30307.0 + s3/30323.0), float(m))
    return r, s1, s2, s3
