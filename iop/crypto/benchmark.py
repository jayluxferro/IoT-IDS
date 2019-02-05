#!/usr/bin/python
"""
Cryptographic time analysis
"""

import db
import sys
import logger as l

def usage():
    print("Usage: python {0} <key length>".format(sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    
    db.resetDB()

    maxLength = int(sys.argv[1])

    l.warning('Generating {0} sets of data'.format(str(maxLength)))
    for _ in range(maxLength):
        # generating oaep data
        for x in range(1, 11):
            db.oaep(x)


        # generating rsa data
        for x in range(1, 11):
            db.rsa(x)
