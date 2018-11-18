#!/usr/bin/python3

import sqlite3

def init():
    return sqlite3.connect('ids.db')

def get_ap():
    conn = init()
    res = conn.cursor().execute('select * from ap limit 1').fetchone()
    conn.close()
    return res

def log(aps, ex, mem, ent, scenario, distance):
    conn = init()
    conn.cursor().execute('insert into scenarios(aps, exec, memory, entropy, scenario, distance) values(?, ?, ?, ?, ?, ?)', (aps, ex, mem, ent, scenario, distance))
    conn.commit()
    conn.close()
