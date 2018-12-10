#!/usr/bin/python

import math
from random import SystemRandom
import sys
import time

gen_set = []
collisions = 0
for x in range(int(sys.argv[1])):
    g = SystemRandom().randint(0, int(sys.argv[1]))
    time.sleep(.1)
    try:
        gen_set.index(g)
    except ValueError:
        # new data
        gen_set.append(g)
        continue
    collisions += 1


print("Collisions " + str(collisions))
