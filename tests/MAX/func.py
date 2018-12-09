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
