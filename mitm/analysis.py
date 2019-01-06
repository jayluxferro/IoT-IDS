#!/usr/bin/python
"""
Author: Jay Lux Ferro
"""

import db
import matplotlib.pyplot as plt
import numpy as np


# cpu usage
x = np.linspace(0, 10, 11)
y = [0]

for c in db.get_cpu():
    y.append(c['usage'])

plt.figure(1)
plt.plot(x, y, '-ro')
plt.grid(True)
plt.xlabel('Attempts')
plt.ylabel('Percentage Overhead (%)')
plt.show()
print("CPU Usage avg: " + str(np.mean(y)))


# detections
y = [0]
for d in db.get_detections():
    y.append(d['time'])

x = np.linspace(0, len(y) - 1, len(y))
plt.figure(2)
plt.plot(x, y, '-o')
plt.grid(True)
plt.xlabel('Attempts')
plt.ylabel('Detection Rate (Seconds)')
plt.show()
print("Avg Detection Rate: " + str(np.mean(y)))


# rtt
y1 = [0]
y2 = [0]
x = np.linspace(0, 10, 11)  

for r in db.get_rtt():
    if r['scenario'] == 0:
        y1.append(r['time'])
    else:
        y2.append(r['time'])

plt.figure(3)
plt.plot(x, y1, '-o', label='Default Mode')
plt.plot(x, y2, '-o', label='MITM Algo')
plt.legend()
plt.ylabel('Round Trip Time (Seconds)')
plt.xlabel('Attempts')
plt.grid(True)
print("Avg RTT, Default: " + str(np.mean(y1)))
print("Avg RTT, MITM Algo: " + str(np.mean(y2)))
plt.show()
