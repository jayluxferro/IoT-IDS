#!/usr/bin/python

import math
import time
import sys
import sqlite3

gen_set = []

bits = int(math.pow(2, 20))



def processData(counter, detection, scenario):
    db = sqlite3.connect('max.db')
    cursor = db.cursor()
    db.execute("insert into detections(counter, detection, scenario) values(?, ?, ?)", (int(counter), float(detection), int(scenario)))
    db.commit()

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
                processData(C, stop - start, sys.argv[2])
                break
                


