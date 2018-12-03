#!/usr/bin/python

import sqlite3

def init():
    return sqlite3.connect('max.db')

def addCollisions(counter, collisions, scenario):
    db = init()
    db.cursor().execute("insert into collisions(counter, collisions, scenario) values(?, ?, ?)", (int(counter), int(collisions), int(scenario)))
    db.commit()

def addDetections(counter, detection, scenario):
    db = init()
    db.cursor().execute("insert into detections(counter, detection, scenario) values(?, ?, ?)", (int(counter), float(detection), int(scenario)))
    db.commit()

def getCollisions():
    db = init()
    return db.cursor().execute("select * from collisions").fetchall()

def getDetections():
    db = init()
    return db.cursor().execute("select * from detections").fetchall()
     
