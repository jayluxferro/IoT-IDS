#!/usr/bin/python

"""
Analysis for system random and wichmann Hill
Random number generation algorithm
"""
import numpy as np
import func
import matplotlib.pyplot as plt

# define params
maxL = 10

srC = []
whC = []

srT = []
whT = []


# collision
for x in range(1, maxL + 1):
    srC.append(len(func.getTotal('sr', x)) - len(func.getDistinct('sr', x)))
    whC.append(len(func.getTotal('wh', x)) - len(func.getDistinct('wh', x)))

    srT.append(func.getAvgTime('sr', x))
    whT.append(func.getAvgTime('wh', x))


x = np.linspace(1, len(srT), len(srT))

print("Avg: sr: {0}".format(str(np.average(srT))))
print("Avg: wh: {0}".format(str(np.average(whT))))
plt.figure(1)
plt.plot(x, srT, '-o', label='System Random')
plt.plot(x, whT, '-o', label='WichmannHill')
plt.legend()
plt.xlabel('Attempts')
plt.ylabel('Computational Time (s)')
plt.grid(True)
plt.show()
