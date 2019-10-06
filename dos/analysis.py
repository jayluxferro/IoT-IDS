#!/usr/bin/python

"""
Author: Jay Lux Ferro
Date:   24th September, 2019
Analysis of DoS Flood
"""

import matplotlib.pyplot as plt
import db
import numpy as np

icmp = []
_udp = []
_tcp = []


for x in db.getP("icmp"):
    icmp.append(x['time'])

for x in db.getP("tcp"):
    _tcp.append(x['time'])

for x in db.getP("udp"):
    _udp.append(x['time'])

icmp = icmp[:50]
_tcp = _tcp[:50]
_udp = _udp[:50]
icmp_it = []
_tcp_it = []
_udp_it = []

#print(len(icmp))
#print(len(_tcp))
#print(len(_udp))

counter = 0
#print(x)
holder = 0
for x in icmp:
    if counter % 2 == 0:
        # the first number
        holder = x
    else:
        icmp_it.append(abs(x - holder))
    counter = counter + 1


counter = 0
holder = 0
for x in _tcp:

    if counter % 2 == 0:
        # the first number
        holder = x
    else:
        _tcp_it.append(abs(x - holder))
    counter = counter + 1



counter = 0
holder = 0
for x in _udp:
    if counter % 2 == 0:
        # the first number
        holder = x
    else:
        _udp_it.append(abs(x - holder))
    counter = counter + 1


## display data
x = np.linspace(1, len(icmp_it), len(icmp_it))

plt.figure(1)
plt.plot(x, icmp_it, '-ro')
plt.axis([0, len(icmp_it), 0, 2])
plt.title('ICMP Flood')
plt.ylabel('Interpacket arrival Time (s)')
plt.xlabel('Attacks')
plt.show()

plt.figure(2)
plt.plot(x, _tcp_it, '-bo')
plt.axis([0, len(icmp_it), 0, 2])
plt.title('TCP Flood')
plt.ylabel('Interpacket arrival Time (s)')
plt.xlabel('Attacks')
plt.show()

plt.figure(3)
plt.plot(x, _udp_it, '-go')
plt.axis([0, len(icmp_it), 0, 2])
plt.title('UDP Flood')
plt.ylabel('Interpacket arrival Time (s)')
plt.xlabel('Attacks')
plt.show()
