#!/usr/bin/python

import func
import time
import math
import sys


def usage():
    print("Usage: python " + sys.argv[0] + " [iterations]")

gen_set = []

collisions = 0
# r, s1, s2, s3 = func.wh64(int(time.time()), int(time.time()) , int(time.time()), 1)



if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    for x in range(int(sys.argv[1])):
        r, s1, s2, s3 = func.wh64(int(time.time()), int(time.time()) , int(time.time()), 1)

        time.sleep(.1)
        try:
            gen_set.index(r)
        except ValueError:
            # new data
            print(r)
            gen_set.append(r)
            continue
        collisions += 1

    print("Collisions " + str(collisions))
    print(gen_set)
    print(len(gen_set))
