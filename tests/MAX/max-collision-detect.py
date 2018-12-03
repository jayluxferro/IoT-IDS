#!/usr/bin/python
"""
Author: Jay Lux Ferro
Email: justiceowusuagyemang@gmail.com/jayluxferro@pm.me
Detect collision in MAX deauth/disassoc algorithm
20 bits
"""
import math
import time
import sys
import sqlite3
import db

gen_set = []
bits = int(math.pow(2, 20))

def usage():
    print("Usage: python " + sys.argv[0] + " [counter: integer] [scenario: integer]")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    for C in range(int(sys.argv[1])):
        X = int(time.time())
        Y = X * 1000
        M = Y * 1000
        generatedNo = ((X * (Y - C) - M + math.factorial(C)) % bits) + 1/(C + 1)
        try:
            gen_set.index(generatedNo)
        except ValueError:
            # new generated No. ; add
            gen_set.append(generatedNo)
            continue
        print("Collision: ", str(generatedNo))

    print(len(gen_set))

    collisions = int(sys.argv[1]) - len(gen_set)
    print("No. of Collisions", collisions)

    # add to db
    db.addCollisions(sys.argv[1], collisions, sys.argv[2])
