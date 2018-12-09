#!/usr/bin/python
"""
Author: Jay Lux Ferro
Email: justiceowusuagyemang@gmail.com/jayluxferro@pm.me
Random Number Generation using Wichmann-Hill pseurandom number generator
20 bits
buffer
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
reset = 0

def usage():
    print("Usage: python " + sys.argv[0] + " [counter: integer] [scenario: integer]")

def generate():
    g = Random() 
    return g.randint(1, bits)

def foundCollision(no):
    try:
        gen_set.index(no)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)


    for x in range(int(sys.argv[1])):
        start = time.time()
        randNo = generate()
        
        if len(gen_set) >= bits:
            gen_set = [] # buffer reset
            reset += 1

        collisionDetected = False
                
        if foundCollision(randNo) == True:
            collisionDetected = True


        while collisionDetected == True:
            randNo = generate()
            if foundCollision(randNo) == False:
                collisionDetected = False
    

        # Validating the collision detection
        if foundCollision(randNo) == True:
            collision += 1

        time_diff = time.time() - start
        usage = func.get_usage()

        db.addWh("wh_buffer", x, sys.argv[2], usage, time_diff)
        
    # store collisions
    db.addCollisions("collisions_buffer", sys.argv[1], collisions, sys.argv[2])
    
    print("Total Collisions: " + str(collisions)) 
    print("Resets: " + str(reset))
