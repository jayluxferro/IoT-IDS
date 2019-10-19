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

# cpu usage analysis
cpuData= [[], [], []] # n1, n2, n3

for x in db.getCPUData():
    cpuData[x['node'] -1].append(x['usage'])

x = np.linspace(1, 87, 87)

plt.figure(1)
plt.plot(x, cpuData[0][:len(x)], '-o', x, cpuData[1][:len(x)], '-o', cpuData[2][:len(x)], '-o')
plt.title('CPU Utilization of nodes before DoS Attack')
plt.xlabel('Number of readings')
plt.ylabel('CPU Utilization (%)')
plt.legend(['N1', 'N2', 'N3'])
#plt.show()

# analyzing dos data
## inter-packet arrival time
icmp = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
tcp  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
udp  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]

scenarios = [1, 2, 3]

for x in scenarios:
    # icmp
    for data in db.getPS("icmp", x):
        node = data['node']
        scn = data['scenario']
        icmp[node - 1][scn - 1].append(data['time'])

    # tcp 
    for data in db.getPS("tcp", x):
        node = data['node']
        scn = data['scenario']
        tcp[node - 1][scn - 1].append(data['time'])

    # udp
    for data in db.getPS("udp", x):
        node = data['node']
        scn = data['scenario']
        udp[node - 1][scn - 1].append(data['time'])

# computing for interpacket arrival time
nodesLegend = ['N1', 'N2', 'N3']
## icmp (fast scenario) -> n -> s
icmp_n1_s1 = f.getInterPacketArrival(icmp[0][0])
icmp_n2_s1 = f.getInterPacketArrival(icmp[1][0])
icmp_n3_s1 = f.getInterPacketArrival(icmp[2][0])

minLen = np.min([ len(icmp_n1_s1), len(icmp_n2_s1), len(icmp_n3_s1) ])
cutOff = 2
x = np.linspace(1, minLen - cutOff, minLen - cutOff)

plt.figure(2)
plt.plot(x, icmp_n1_s1[cutOff:minLen], '-o', x, icmp_n2_s1[cutOff:minLen], '-o', x, icmp_n3_s1[cutOff:minLen], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (10pkts/sec)')

## icmp (faster scenario) -> n -> s
icmp_n1_s2 = f.getInterPacketArrival(icmp[0][1])
icmp_n2_s2 = f.getInterPacketArrival(icmp[1][1])
icmp_n3_s2 = f.getInterPacketArrival(icmp[2][1])

minLen_n_s2 = np.min([ len(icmp_n1_s2), len(icmp_n2_s2), len(icmp_n3_s2) ])
cutOff_n_s2 = 0

x_n_s2 = np.linspace(1, minLen_n_s2 - cutOff_n_s2, minLen_n_s2 - cutOff_n_s2)

plt.figure(3)
plt.plot(x_n_s2, icmp_n1_s2[cutOff_n_s2:minLen_n_s2], '-o', x_n_s2, icmp_n2_s2[cutOff_n_s2:minLen_n_s2], '-o', x_n_s2, icmp_n3_s2[cutOff_n_s2:minLen_n_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (100pkts/sec)')

## icmp (random scenarios - AFAP) -> n -> s
icmp_n1_s3 = f.getInterPacketArrival(icmp[0][2])
icmp_n2_s3 = f.getInterPacketArrival(icmp[1][2])
icmp_n3_s3 = f.getInterPacketArrival(icmp[2][2])

minLen_n_s3 = np.min([ len(icmp_n1_s3), len(icmp_n2_s3), len(icmp_n2_s3) ])
cutOff_n_s3 = 0

x_n_s3 = np.linspace(1, minLen_n_s3 - cutOff_n_s3, minLen_n_s3 - cutOff_n_s3)

plt.figure(4)
plt.plot(x_n_s3, icmp_n1_s3[cutOff_n_s3:minLen_n_s3], '-o', x_n_s3, icmp_n2_s3[cutOff_n_s3:minLen_n_s3], '-o', x_n_s3, icmp_n3_s3[cutOff_n_s3:minLen_n_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (Random - AFAP)')


## TCP (Inter-Packet Arrival Time)
### TCP (fast scenario) n -> s
tcp_n1_s1 = f.getInterPacketArrival(tcp[0][0])
tcp_n2_s1 = f.getInterPacketArrival(tcp[1][0])
tcp_n3_s1 = f.getInterPacketArrival(tcp[2][0])

# trim outliers
tcp_n1_s1 = f.trimOutliers(tcp_n1_s1, 2)
tcp_n2_s1 = f.trimOutliers(tcp_n2_s1, 2)
tcp_n3_s1 = f.trimOutliers(tcp_n3_s1, 2)

minLen_t_s1 = np.min([ len(tcp_n1_s1), len(tcp_n2_s1), len(tcp_n3_s1) ])

cutOff_t_s1 = 0

xt_n_s1 = np.linspace(1, minLen_t_s1 - cutOff_t_s1, minLen_t_s1 - cutOff_t_s1)

plt.figure(5)
plt.plot(xt_n_s1, tcp_n1_s1[cutOff_t_s1:minLen_t_s1], '-o', xt_n_s1, tcp_n2_s1[cutOff_t_s1:minLen_t_s1], '-o', xt_n_s1, tcp_n3_s1[cutOff_t_s1:minLen_t_s1], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (10pkts/sec)')

### TCP (faster scenario) n -> s
tcp_n1_s2 = f.getInterPacketArrival(tcp[0][1])
tcp_n2_s2 = f.getInterPacketArrival(tcp[1][1])
tcp_n3_s2 = f.getInterPacketArrival(tcp[2][1])

minLen_t_s2 = np.min([ len(tcp_n1_s2), len(tcp_n2_s2), len(tcp_n3_s2) ])

xt_n_s2 = np.linspace(1, minLen_t_s2, minLen_t_s2)

plt.figure(6)
plt.plot(xt_n_s2, tcp_n1_s2[:minLen_t_s2], '-o', xt_n_s2, tcp_n2_s2[:minLen_t_s2], '-o', xt_n_s2, tcp_n3_s2[:minLen_t_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (100pkts/sec)')

### TCP (Random scenario) n -> s
tcp_n1_s3 = f.getInterPacketArrival(tcp[0][2])
tcp_n2_s3 = f.getInterPacketArrival(tcp[1][2])
tcp_n3_s3 = f.getInterPacketArrival(tcp[2][2])

minLen_t_s3 = np.min([ len(tcp_n1_s3), len(tcp_n2_s3), len(tcp_n3_s3) ])

xt_n_s3 = np.linspace(1, minLen_t_s3, minLen_t_s3)

plt.figure(7)
plt.plot(xt_n_s3, tcp_n1_s3[:minLen_t_s3], '-o', xt_n_s3, tcp_n2_s3[:minLen_t_s3], '-o', xt_n_s3, tcp_n3_s3[:minLen_t_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (Random - AFAP)')

## UDP Inter-Packet Arrival Time
### UDP (fast scenario) n -> s
udp_n1_s1 = f.getInterPacketArrival(udp[0][0])
udp_n2_s1 = f.getInterPacketArrival(udp[1][0])
udp_n3_s1 = f.getInterPacketArrival(udp[2][0])

# remove outliers
udp_n1_s1 = f.trimOutliers(udp_n1_s1, 2)
udp_n2_s1 = f.trimOutliers(udp_n2_s1, 2)
udp_n3_s1 = f.trimOutliers(udp_n3_s1, 3)

minLen_u_s1 = np.min([ len(udp_n1_s1), len(udp_n2_s1), len(udp_n3_s1) ])

xu_n_s1 = np.linspace(1, minLen_u_s1, minLen_u_s1)

plt.figure(8)
plt.plot(xu_n_s1, udp_n1_s1[:minLen_u_s1], '-o', xu_n_s1, udp_n2_s1[:minLen_u_s1], '-o', xu_n_s1, udp_n3_s1[:minLen_u_s1], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for UDP Flood Attack (10pkts/sec)')

### UDP (faster scenario) n -> s
udp_n1_s2 = f.getInterPacketArrival(udp[0][1])
udp_n2_s2 = f.getInterPacketArrival(udp[1][1])
udp_n3_s2 = f.getInterPacketArrival(udp[2][1])

minLen_u_s2 = np.min([ len(udp_n1_s2), len(udp_n2_s2), len(udp_n3_s2) ])

xu_n_s2 = np.linspace(1, minLen_u_s2, minLen_u_s2)

plt.figure(9)
plt.plot(xu_n_s2, udp_n1_s2[:minLen_u_s2], '-o', xu_n_s2, udp_n2_s2[:minLen_u_s2], '-o', xu_n_s2, udp_n3_s2[:minLen_u_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for UDP Flood Attack (100pkts/sec)') 

### UDP (Random - AFAP) n -> s
udp_n1_s3 = f.getInterPacketArrival(udp[0][2])
udp_n2_s3 = f.getInterPacketArrival(udp[1][2])
udp_n3_s3 = f.getInterPacketArrival(udp[2][2])

# removing outliers
udp_n1_s3 = f.trimOutliers(udp_n1_s3, 1)
udp_n2_s3 = f.trimOutliers(udp_n2_s3, 2)
udp_n3_s3 = f.trimOutliers(udp_n3_s3, 1)

minLen_u_s3 = np.min([ len(udp_n1_s3), len(udp_n2_s3), len(udp_n3_s3) ])

xu_n_s3 = np.linspace(1, minLen_u_s3, minLen_u_s3)

plt.figure(10)
plt.plot(xu_n_s3, udp_n1_s3[:minLen_u_s3], '-o', xu_n_s3, udp_n2_s3[:minLen_u_s3], '-o', xu_n_s3, udp_n3_s3[:minLen_u_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival time for UDP Flood Attack (Random - AFAP)')



# display all graphs 
plt.show()
