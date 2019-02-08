#!/usr/bin/python

"""
System Random and Winchmann Hill Random algo test
1000 iterations
"""
import sys
import func

def usage():
    print("python {0} <maxLength of characters>".format(str(sys.argv[0])))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage()

    maxL = int(sys.argv[1]) + 1

    # deleting data
    func.deleteData()

    for x in range(0, 1000):
        for y in range(1, maxL):
            func.sr(y)
            func.wh(y)



