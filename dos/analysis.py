#!/usr/bin/python

"""
Author: Jay Lux Ferro
Date:   24th September, 2019
Analysis of DoS Flood
"""

import matplotlib.pyplot as plt
import db
import numpy as np
import func as f

icmp_1 = []
icmp_2 = []
icmp_3 = []


_udp_1 = []
_udp_2 = []
_udp_3 = []


_tcp_1 = []
_tcp_2 = []
_tcp_3 = []

# fetch data
for x in db.getP("icmp"):
    if x['scenario'] == 1:
        icmp_1.append(x['time'])

    elif x['scenario'] == 2:
        icmp_2.append(x['time'])

    elif x['scenario'] == 3:
        icmp_3.append(x['time'])
    
    else: 
        pass

for x in db.getP("tcp"):
    if x['scenario'] == 1:
        _tcp_1.append(x['time'])

    elif x['scenario'] == 2:
        _tcp_2.append(x['time'])

    elif x['scenario'] == 3:
        _tcp_3.append(x['time'])
    
    else: 
        pass

for x in db.getP("udp"):
    if x['scenario'] == 1:
        _udp_1.append(x['time'])

    elif x['scenario'] == 2:
        _udp_2.append(x['time'])

    elif x['scenario'] == 3:
        _udp_3.append(x['time'])
    
    else: 
        pass


## formatting data
maxDataLength = 250
# icmp
icmp_1 = f.getInterPacketArrival(icmp_1[:maxDataLength])
icmp_2 = f.getInterPacketArrival(icmp_2[:maxDataLength])
icmp_3 = f.getInterPacketArrival(icmp_3[:maxDataLength])

# tcp
tcp_1 = f.getInterPacketArrival(_tcp_1[:maxDataLength])
tcp_2 = f.getInterPacketArrival(_tcp_2[:maxDataLength])
tcp_3 = f.getInterPacketArrival(_tcp_3[:maxDataLength])

#udp
udp_1 = f.getInterPacketArrival(_udp_1[:maxDataLength])
udp_2 = f.getInterPacketArrival(_udp_2[:maxDataLength])
udp_3 = f.getInterPacketArrival(_udp_3[:maxDataLength])


# icmp
x1 = np.linspace(1, len(icmp_1), len(icmp_1))
x2 = np.linspace(1, len(icmp_2), len(icmp_2))
x3 = np.linspace(1, len(icmp_3), len(icmp_3))

mean = [np.mean(icmp_1), np.mean(icmp_2), np.mean(icmp_3)]
icmp_mean = np.mean(mean)
print(icmp_mean)
plt.figure(1)
plt.plot(x1, icmp_1, '-o', x2, icmp_2, '-o', x3, icmp_3, '-o')
plt.grid(axis='both')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Floods')
plt.ylabel('Inter-packet Arrival Time')
plt.title('ICMP Flood')
plt.show()

# tcp
x1 = np.linspace(1, len(tcp_1), len(tcp_1))
x2 = np.linspace(1, len(tcp_2), len(tcp_2))
x3 = np.linspace(1, len(tcp_3), len(tcp_3))

mean = [np.mean(tcp_1), np.mean(tcp_2), np.mean(tcp_3)]
tcp_mean = np.mean(mean)
print(icmp_mean)

plt.figure(2)
plt.plot(x1, tcp_1, '-o', x2, tcp_2, '-o', x3, tcp_3, '-o')
plt.grid(axis='both')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Floods')
plt.ylabel('Inter-packet Arrival Time')
plt.title('TCP Flood')
plt.show()

# udp
x1 = np.linspace(1, len(udp_1), len(udp_1))
x2 = np.linspace(1, len(udp_2), len(udp_2))
x3 = np.linspace(1, len(udp_3), len(udp_3))

mean = [np.mean(udp_1), np.mean(udp_2), np.mean(udp_3)]
udp_mean = np.mean(mean)
print(icmp_mean)

plt.figure(3)
plt.plot(x1, udp_1, '-o', x2, udp_2, '-o', x3, udp_3, '-o')
plt.grid(axis='both')
plt.legend(['N1', 'N2', 'N3'])
plt.xlabel('Floods')
plt.ylabel('Inter-packet Arrival Time')
plt.title('UDP Flood')
plt.show()
