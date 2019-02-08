#!/usr/bin/python

import db
import matplotlib.pyplot as plt
import numpy as np

cpu = []
attempts = np.linspace(1, 10, 10)

for x in db.getCPU():
    cpu.append(x['percent'])

## cpu
plt.figure(1)
plt.plot(attempts, cpu, '-ro')
plt.xlabel('Attempts')
plt.ylabel('CPU Usage (%)')
plt.grid(True)
print("Avg: {0}".format(str(np.average(cpu))))
plt.show()



## Revocation/Restoration Time
r1 = []
r2 = []

for x in db.getRevocation(0):
    r1.append(x['time'])


for x in db.getRevocation(1):
    r2.append(x['time'])

attempts = np.linspace(1, len(r1), len(r1))

plt.figure(2)
plt.plot(attempts, r1, '-o', label='Revocation')
plt.plot(attempts, r2, '-o', label='Restoration')
plt.legend()
plt.grid(True)
plt.ylabel('Revocation/Restoration Time (s)')
print('Avg revocation time: {0}'.format(str(np.average(r1))))
print('Avg restoration time: {0}'.format(str(np.average(r2))))
plt.show()
