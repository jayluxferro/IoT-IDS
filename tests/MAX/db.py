#!/usr/bin/python

import sqlite3

def init():
    return sqlite3.connect('max.db')

def addCollisions(table, counter, collisions, scenario):
    db = init()
    db.cursor().execute("insert into "+ table + "(counter, collisions, scenario) values(?, ?, ?)", (int(counter), int(collisions), int(scenario)))
    db.commit()

def addWh(table, counter, scenario, percent, time):
    db = init()
    db.cursor().execute("insert into " + table + "(counter, scenario, percent, time) values(?, ?, ?, ?)", (int(counter), int(scenario), float(percent), float(time)))
    db.commit()     
