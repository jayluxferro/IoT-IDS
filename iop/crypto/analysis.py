#!/usr/bin/python

"""
RSA and OAEP benchmark analysis
"""

import db
import numpy as np
import matplotlib.pyplot as plt

keyLength = np.linspace(1024, 10240, 10)

# OAEP
oaep = []
for x in range(1, 11):
    oaep.append(db.getAlgo('oaep', x)[0])

# RSA
rsa = []
for x in range(1, 11):
    rsa.append(db.getAlgo('rsa', x)[0])


plt.figure(1)
plt.plot(keyLength, oaep, '-o', label='RSA with OAEP')
plt.plot(keyLength, rsa, '-o', label='RSA with no OAEP')
plt.legend()
plt.grid(True)
plt.xlabel('Key Length')
plt.ylabel('Average Computational Time (s)')
plt.show()


plt.figure(2)
plt.plot(keyLength, oaep, '-o')
plt.xlabel('Key Length')
plt.ylabel('Average Computational Time (s)')
plt.grid(True)
plt.show()


plt.figure(3)
plt.plot(keyLength, rsa, '-o')
plt.xlabel('Key Length')
plt.ylabel('Average Computational Time (s)')
plt.grid(True)
plt.show()
