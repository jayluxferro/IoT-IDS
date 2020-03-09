#!/usr/bin/python

"""
Test of random using system random and 
wichmann-hill random number generation algorithm
"""
import logger as l
from random import SystemRandom, WichmannHill
import sqlite3
import time
from binascii import hexlify

def init():
    con = sqlite3.connect('db.db')
    con.row_factory = sqlite3.Row
    return con


def addData(category, data, length, time):
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into msg(category, data, length, time) values(?, ?, ?, ?)", (category, data, length, time))
    db.commit()
    l.success('Added data\n')


def sr(length):
    start = time.time()
    data = SystemRandom().randint(0x0000, 0xffff)
    stop = time.time()
    addData("sr", data, length, stop - start)


def wh(length):
    start = time.time()
    data = WichmannHill().randint(0x0000, 0xffff)
    stop = time.time()
    addData("wh", data, length, stop - start)


def deleteData():
    db = init()
    cursor = db.cursor()
    cursor.execute("delete from msg")
    db.commit()
    l.warning('Deleted data')


def getDistinct(category, length):
    db = init()
    cursor = db.cursor()
    cursor.execute("select distinct(data) from msg where category=? and length=?", (category, length))
    return cursor.fetchall()

def getTotal(category, length):
    db = init()
    cursor = db.cursor()
    cursor.execute("select * from msg where category=? and length=?", (category, length))
    return cursor.fetchall()

def getAvgTime(category, length):
    db = init()
    cursor = db.cursor()
    cursor.execute("select avg(time) from msg where category=? and length=?", (category, length))
    return cursor.fetchone()[0]

