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
import func

gen_set = []
bits = int(math.pow(2, 20))
collisions = 0

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
        generatedNo = int(((X * (Y - C) - M + math.factorial(C)) % bits) + 1/(C + 1))
        
        print(str(generatedNo) + ": " + str(func.get_usage()) + "%")
        try:
            gen_set.index(generatedNo)
        except ValueError:
            gen_set.append(generatedNo)
            continue

        # collision found
        collisions += 1
    print("Collisions detected: " + str(collisions))
