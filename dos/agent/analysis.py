#!/usr/bin/python
"""
Analysis
"""

import db
import matplotlib.pyplot as plt
import numpy as np

# CPU Data
n1_normal = [[], []] # cpu, mem
n1_active = [[], []]
n2_normal = [[], []]
n2_active = [[], []]
n3_normal = [[], []]
n3_active = [[], []]


for x in db.getTable("cpu"):
    if x['node'] == 1:
        if x['scenario'] == 0:
            n1_normal[0].append(x['cpu'])
            n1_normal[1].append(x['mem'])
        else:
            n1_active[0].append(x['cpu'])
            n1_active[1].append(x['mem'])
    elif x['node'] == 2:
        if x['scenario'] == 0:
            n2_normal[0].append(x['cpu'])
            n2_normal[1].append(x['mem'])
        else:
            n2_active[0].append(x['cpu'])
            n2_active[1].append(x['mem'])
    elif x['node'] == 3:
        if x['scenario'] == 0:
            n3_normal[0].append(x['cpu'])
            n3_normal[1].append(x['mem'])
        else:
            n3_active[0].append(x['cpu'])
            n3_active[1].append(x['mem'])

maxPoints = 20
x = np.linspace(1, maxPoints - 1, maxPoints - 1)
plt.figure()
plt.plot(x, n1_normal[0][1:maxPoints], '-o', x, n1_active[0][1:maxPoints], '-o')
plt.legend(['N1 - Normal', 'N1 - Active'])
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.show()


plt.figure()
plt.plot(x, n2_normal[0][1:maxPoints], '-o', x, n2_active[0][1:maxPoints], '-o')
plt.legend(['N2 - Normal', 'N2 - Active'])
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.show()


plt.figure()
plt.plot(x, n3_normal[0][1:maxPoints], '-o', x, n3_active[0][1:maxPoints], '-o')
plt.legend(['N3 - Normal', 'N3 - Active'])
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.show()

## memory
plt.figure()
plt.plot(x, n1_normal[1][1:maxPoints], '-o', x, n1_active[1][1:maxPoints], '-o')
plt.legend(['N1 - Normal', 'N1 - Active'])
plt.xlabel('Number of times')
plt.ylabel('Memory Utilization (%)')
plt.show()


plt.figure()
plt.plot(x, n2_normal[1][1:maxPoints], '-o', x, n2_active[1][1:maxPoints], '-o')
plt.legend(['N2 - Normal', 'N2 - Active'])
plt.xlabel('Number of times')
plt.ylabel('Memory Utilization (%)')
plt.show()


plt.figure()
plt.plot(x, n3_normal[1][1:maxPoints], '-o', x, n3_active[1][1:maxPoints], '-o')
plt.legend(['N3 - Normal', 'N3 - Active'])
plt.xlabel('Number of times')
plt.ylabel('Memory Utilization (%)')
plt.show()

# Detection
icmp = [[], [], []] # n1, n2, n3
tcp = [[], [], []]
udp = [[], [], []]

for x in db.getTable("detection"):
    if x['proto'] == 'icmp':
        if x['node'] == 1:
            icmp[0].append(x['time'])
        elif x['node'] == 2:
            icmp[1].append(x['time'])
        elif x['node'] == 3:
            icmp[2].append(x['time'])
    elif x['proto'] == 'tcp':
        if x['node'] == 1:
            tcp[0].append(x['time'])
        elif x['node'] == 2:
            tcp[1].append(x['time'])
        elif x['node'] == 3:
            tcp[2].append(x['time'])
    elif x['proto'] == 'udp':
        if x['node'] == 1:
            udp[0].append(x['time'])
        elif x['node'] == 2:
            udp[1].append(x['time'])
        elif x['node'] == 3:
            udp[2].append(x['time'])

maxPoints = 10
x = np.linspace(1, maxPoints - 1, maxPoints - 1)

plt.figure()
plt.plot(x, icmp[0][1: maxPoints], '-o', x, icmp[1][1:maxPoints], '-o', x, icmp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()


plt.figure()
plt.plot(x, tcp[0][1: maxPoints], '-o', x, tcp[1][1:maxPoints], '-o', x, tcp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()

plt.figure()
plt.plot(x, udp[0][1: maxPoints], '-o', x, udp[1][1:maxPoints], '-o', x, udp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()


# Defense
icmp = [[], [], []] # n1, n2, n3
tcp = [[], [], []]
udp = [[], [], []]

for x in db.getTable("defense"):
    if x['proto'] == 'icmp':
        if x['node'] == 1:
            icmp[0].append(x['time'])
        elif x['node'] == 2:
            icmp[1].append(x['time'])
        elif x['node'] == 3:
            icmp[2].append(x['time'])
    elif x['proto'] == 'tcp':
        if x['node'] == 1:
            tcp[0].append(x['time'])
        elif x['node'] == 2:
            tcp[1].append(x['time'])
        elif x['node'] == 3:
            tcp[2].append(x['time'])
    elif x['proto'] == 'udp':
        if x['node'] == 1:
            udp[0].append(x['time'])
        elif x['node'] == 2:
            udp[1].append(x['time'])
        elif x['node'] == 3:
            udp[2].append(x['time'])

maxPoints = 10
x = np.linspace(1, maxPoints - 1, maxPoints - 1)

plt.figure()
plt.plot(x, icmp[0][1: maxPoints], '-o', x, icmp[1][1:maxPoints], '-o', x, icmp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()


plt.figure()
plt.plot(x, tcp[0][1: maxPoints], '-o', x, tcp[1][1:maxPoints], '-o', x, tcp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()

plt.figure()
plt.plot(x, udp[0][1: maxPoints], '-o', x, udp[1][1:maxPoints], '-o', x, udp[2][1:maxPoints], '-o')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Number of times')
plt.ylabel('Detection Time')
plt.show()

