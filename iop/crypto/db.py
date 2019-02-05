#!/usr/bin/python

"""
Database Handler
"""

import sqlite3
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import time
import logger as l

def init():
    con = sqlite3.connect('crypto.db')
    con.row_factory = sqlite3.Row
    return con


def oaep(length):
    l.default('OAEP, Generating key {0}'.format(str(length)))
    start = time.time()
    random_generator = Random.new().read
    rsakey = RSA.generate(1024 * length, random_generator)
    pubCipher = PKCS1_OAEP.new(rsakey.publickey())
    privCipher = PKCS1_OAEP.new(rsakey)
    end = time.time()
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into algo(category, len, time) values(?, ?, ?)", ('oaep', length, end - start))
    db.commit()
    l.success('Done...')
    print('\n')


def rsa(length):
    l.default('RSA, Generating key {0}'.format(str(length)))
    start = time.time()
    rsakey = RSA.generate(1024 * 1, Random.new().read)
    pubCipher = rsakey.publickey()
    privCipher = rsakey
    end = time.time()
    db = init()
    cursor = db.cursor()
    cursor.execute("insert into algo(category, len, time) values(?, ?, ?)", ('rsa', length, end - start))
    db.commit()
    l.success('done...')
    print('\n')
   

def resetDB():
    db = init()
    cursor = db.cursor()
    cursor.execute("delete from algo")
    db.commit()
    l.warning('Cleared database')


def getAlgo(category, length):
    db = init()
    cursor = db.cursor()
    cursor.execute("select avg(time) from algo where category=? and len=?", (category, length))
    return cursor.fetchone()
