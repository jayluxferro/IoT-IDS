#!/usr/bin/python
"""
Author: Jay Lux Ferro
Email: justiceowusuagyemang@gmail.com/jayluxferro@pm.me
Measure the time it takes to regenerate a MAX random number
20 bits
"""
import math
import time
import sys
import sqlite3
import db

#default params
gen_set = []

bits = int(math.pow(2, 20))

def usage():
    print("Usage: python " + sys.argv[0] + " [counter: integer] [scenario: int]")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    for C in range(int(sys.argv[1])):
        start = time.time()
        X = int(time.time())
        Y = X * 1000
        M = Y * 1000
        generatedNo = ((X * (Y - C) - M + math.factorial(C)) % bits) + 1/(C + 1)
        try:
            gen_set.index(generatedNo)
        except ValueError:
            # new generated No. ; add
            gen_set.append(generatedNo)
            for c in range(bits):
                if c == int(generatedNo):
                    stop = time.time()
                    print("Found: ", c)
                    db.addDetections(C, stop - start, sys.argv[2])
                    break
                


