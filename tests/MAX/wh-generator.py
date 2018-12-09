#!/usr/bin/python
"""
Author: Jay Lux Ferro
Email: justiceowusuagyemang@gmail.com/jayluxferro@pm.me
Random Number Generation using Wichmann-Hill pseurandom number generator
20 bits
"""
import math
import time
import sys
import sqlite3
import db
from random import Random
import func

gen_set = []
bits = int(math.pow(2, 20))
collisions = 0

def usage():
    print("Usage: python " + sys.argv[0] + " [counter: integer] [scenario: integer]")

def generate(g):
    return g.randint(1, bits)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)


    for x in range(int(sys.argv[1])):
        start = time.time()
        g = Random()
        randNo = generate(g)
        time_diff = time.time() - start
        usage = func.get_usage()
        

        # add stats to db
        db.addWh("wh", x, sys.argv[2], usage, time_diff)

        try:
            gen_set.index(randNo)
        except ValueError:
            # new data
            gen_set.append(randNo)
            continue

        collisions += 1
        print("Collision: " + str(randNo))
    
    # store collisions
    db.addCollisions("collisions", sys.argv[1], collisions, sys.argv[2])
    
    print("Total Collisions: " + str(collisions)) 
