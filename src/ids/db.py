#!/usr/bin/python3

import sqlite3

def init():
    return sqlite3.connect('ids.db')

def get_ap():
    conn = init()
    res = conn.cursor().execute('select * from ap limit 1').fetchone()
    conn.close()
    return res

def log(aps, ex, mem, ent):
    conn = init()
    conn.cursor().execute('insert into single(aps, exec, memory, entropy) values(?, ?, ?, ?)', (aps, ex, mem, ent))
    conn.commit()
    conn.close()
