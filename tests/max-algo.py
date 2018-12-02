#!/usr/bin/python

import math
import time
import sys
import sqlite3

gen_set = []
bits = int(math.pow(2, 20))
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

db = sqlite3.connect('max.db')
cursor = db.cursor()
db.execute("insert into collisions(counter, collisions, scenario) values(?, ?, ?)", (int(sys.argv[1]), collisions, int(sys.argv[2]))) 
db.commit()
