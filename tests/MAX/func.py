#!/usr/bin/python

import db

def getDetectionsAvg(start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select avg(detection) from detections where counter >= ? and counter <= ? and scenario=?", (start, stop, scenario)).fetchone()[0]

def getCollisionsAvg(start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select avg(collisions) from collisions where counter >=? and counter <=? and scenario=?", (start, stop, scenario)).fetchone()[0]

def getCollisionsSum(start, stop, scenario):
    conn = db.init()
    return conn.cursor().execute("select sum(collisions) from collisions where counter >=? and counter <=? and scenario = ?", (start, stop, scenario)).fetchone()[0]
