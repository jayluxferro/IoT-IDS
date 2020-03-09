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
import sys

# cpu usage analysis
cpuData= [[[], [], []], [[], [], []], [[], [], []]] # n1, n2, n3

for scenario in range(1, 4):
    for node in range(1, 4):
        for data in db.getCPUData(node, scenario):
            n = node - 1
            scn = scenario - 1
            cpuData[n][scn].append(data['cpu_percent'])

cpuLegend = ['S1', 'S2', 'S3']
cpuLegend2 = ['N1', 'N2', 'N3']
"""
# cpu usage -> n1
cpuData_n1 = cpuData[0]
minLen_cpu_n1 = np.min([ len(cpuData_n1[0]), len(cpuData_n1[1]), len(cpuData_n1[2]) ])

x = np.linspace(1, minLen_cpu_n1, minLen_cpu_n1)

plt.figure()
plt.plot(x, cpuData_n1[0][:minLen_cpu_n1], '-o', x, cpuData_n1[1][:minLen_cpu_n1], '-o', x, cpuData_n1[2][:minLen_cpu_n1], '-o')
plt.legend(cpuLegend)
plt.title('CPU Utilization for Node 1')
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.show()

# cpu usage -> n2
cpuData_n2 = cpuData[1]
minLen_cpu_n2 = np.min([ len(cpuData_n2[0]), len(cpuData_n2[1]), len(cpuData_n2[2]) ])
x = np.linspace(1, minLen_cpu_n2, minLen_cpu_n2)

plt.figure()
plt.plot(x, cpuData_n2[0][:minLen_cpu_n2], '-o', x, cpuData_n2[1][:minLen_cpu_n2], '-o', x, cpuData_n2[2][:minLen_cpu_n2], '-o')
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.title('CPU Utilization for Node 2')
plt.legend(cpuLegend)
plt.show()

# cpu usage -> n3
cpuData_n3 = cpuData[2]
minLen_cpu_n3 = np.min([ len(cpuData_n3[0]), len(cpuData_n3[1]), len(cpuData_n3[2]) ])
x = np.linspace(1, minLen_cpu_n3, minLen_cpu_n3)

plt.figure()
plt.plot(x, cpuData_n3[0][:minLen_cpu_n3], '-o', x, cpuData_n3[1][:minLen_cpu_n3], '-o', x, cpuData_n3[2][:minLen_cpu_n3], '-o')
plt.xlabel('Number of times')
plt.ylabel('CPU Utilization (%)')
plt.title('CPU Utilization of Node 3')
plt.legend(cpuLegend)
plt.show()
"""
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
mean_x = [1, 2, 3]
## icmp (fast scenario) -> n -> s
icmp_n1_s1 = f.getInterPacketArrival(icmp[0][0])
icmp_n2_s1 = f.getInterPacketArrival(icmp[1][0])
icmp_n3_s1 = f.getInterPacketArrival(icmp[2][0])
mean_icmp_n1_s1 = np.mean(icmp_n1_s1)
mean_icmp_n2_s1 = np.mean(icmp_n2_s1)
mean_icmp_n3_s1 = np.mean(icmp_n3_s1)

minLen = np.min([ len(icmp_n1_s1), len(icmp_n2_s1), len(icmp_n3_s1) ])
cutOff = 2
x = np.linspace(1, minLen - cutOff, minLen - cutOff)

plt.figure()
plt.plot(x, icmp_n1_s1[cutOff:minLen], '-o', x, icmp_n2_s1[cutOff:minLen], '-o', x, icmp_n3_s1[cutOff:minLen], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (10pkts/sec)')
print("icmp (fast scn) -> n -> s ", mean_icmp_n1_s1, mean_icmp_n2_s1, mean_icmp_n3_s1) 
print("icmp (fast scn) -> n -> s (min, max)", (np.min(icmp_n1_s1), np.max(icmp_n1_s1)), (np.min(icmp_n2_s1), np.max(icmp_n2_s1)), (np.min(icmp_n3_s1), np.max(icmp_n3_s1)))
print("")
plt.show()


## icmp (faster scenario) -> n -> s
icmp_n1_s2 = f.getInterPacketArrival(icmp[0][1])
icmp_n2_s2 = f.getInterPacketArrival(icmp[1][1])
icmp_n3_s2 = f.getInterPacketArrival(icmp[2][1])
mean_icmp_n1_s2 = np.mean(icmp_n1_s2)
mean_icmp_n2_s2 = np.mean(icmp_n2_s2)
mean_icmp_n3_s2 = np.mean(icmp_n3_s2)

print("icmp (faster scn) -> n -> s ", mean_icmp_n1_s2, mean_icmp_n2_s2, mean_icmp_n3_s2) 
print("icmp (faster scn) -> n -> s (min, max) ", (np.min(icmp_n1_s2), np.max(icmp_n1_s2)), (np.min(icmp_n2_s2), np.max(icmp_n2_s2)), (np.min(icmp_n3_s2), np.max(icmp_n3_s2)))
print("")
minLen_n_s2 = np.min([ len(icmp_n1_s2), len(icmp_n2_s2), len(icmp_n3_s2) ])
cutOff_n_s2 = 0

x_n_s2 = np.linspace(1, minLen_n_s2 - cutOff_n_s2, minLen_n_s2 - cutOff_n_s2)

plt.figure()
plt.plot(x_n_s2, icmp_n1_s2[cutOff_n_s2:minLen_n_s2], '-o', x_n_s2, icmp_n2_s2[cutOff_n_s2:minLen_n_s2], '-o', x_n_s2, icmp_n3_s2[cutOff_n_s2:minLen_n_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (100pkts/sec)')
plt.show()

## icmp (random scenarios - AFAP) -> n -> s
icmp_n1_s3 = f.getInterPacketArrival(icmp[0][2])
icmp_n2_s3 = f.getInterPacketArrival(icmp[1][2])
icmp_n3_s3 = f.getInterPacketArrival(icmp[2][2])

mean_icmp_n1_s3 = np.mean(icmp_n1_s3)
mean_icmp_n2_s3 = np.mean(icmp_n2_s3)
mean_icmp_n3_s3 = np.mean(icmp_n3_s3)

print("icmp (random scn) -> n -> s ", mean_icmp_n1_s3, mean_icmp_n2_s3, mean_icmp_n3_s3) 
print("icmp (random scn) -> n -> s (min, max) ", (np.min(icmp_n1_s3), np.max(icmp_n1_s3)), (np.min(icmp_n2_s3), np.max(icmp_n2_s3)), (np.min(icmp_n3_s3), np.max(icmp_n3_s3)))
print("")
minLen_n_s3 = np.min([ len(icmp_n1_s3), len(icmp_n2_s3), len(icmp_n2_s3) ])
cutOff_n_s3 = 0

x_n_s3 = np.linspace(1, minLen_n_s3 - cutOff_n_s3, minLen_n_s3 - cutOff_n_s3)

plt.figure()
plt.plot(x_n_s3, icmp_n1_s3[cutOff_n_s3:minLen_n_s3], '-o', x_n_s3, icmp_n2_s3[cutOff_n_s3:minLen_n_s3], '-o', x_n_s3, icmp_n3_s3[cutOff_n_s3:minLen_n_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for ICMP Flood Attack (Random - AFAP)')
plt.show()

## icmp (mean ipat)
plt.figure()
plt.plot(mean_x, [mean_icmp_n1_s1, mean_icmp_n2_s1, mean_icmp_n3_s1], '-o', mean_x, [mean_icmp_n1_s2, mean_icmp_n2_s2, mean_icmp_n3_s2], '-o', mean_x, [mean_icmp_n1_s3, mean_icmp_n2_s3, mean_icmp_n3_s3], '-o')
plt.xlabel('Scenarios')
plt.ylabel('Average Inter-Packet Arrival Time (s)')
plt.title('Average Inter-Packet Arrival Time for ICMP Flood Attack')
plt.legend(cpuLegend)
plt.show()

## TCP (Inter-Packet Arrival Time)
### TCP (fast scenario) n -> s
tcp_n1_s1 = f.getInterPacketArrival(tcp[0][0])
tcp_n2_s1 = f.getInterPacketArrival(tcp[1][0])
tcp_n3_s1 = f.getInterPacketArrival(tcp[2][0])

# trim outliers
tcp_n1_s1 = f.trimOutliers(tcp_n1_s1, 2)
tcp_n2_s1 = f.trimOutliers(tcp_n2_s1, 2)
tcp_n3_s1 = f.trimOutliers(tcp_n3_s1, 2)

mean_tcp_n1_s1 = np.mean(tcp_n1_s1)
mean_tcp_n2_s1 = np.mean(tcp_n2_s1)
mean_tcp_n3_s1 = np.mean(tcp_n3_s1)

print("tcp (fast scn) -> n -> s ", mean_tcp_n1_s1, mean_tcp_n2_s1, mean_tcp_n3_s1) 
print("tcp (fast scn) -> n -> s (min, max) ", (np.min(tcp_n1_s1), np.max(tcp_n1_s1)), (np.min(tcp_n2_s1), np.max(tcp_n2_s1)), (np.min(tcp_n3_s1), np.max(tcp_n3_s1)))
print("")
minLen_t_s1 = np.min([ len(tcp_n1_s1), len(tcp_n2_s1), len(tcp_n3_s1) ])

cutOff_t_s1 = 0

xt_n_s1 = np.linspace(1, minLen_t_s1 - cutOff_t_s1, minLen_t_s1 - cutOff_t_s1)

plt.figure()
plt.plot(xt_n_s1, tcp_n1_s1[cutOff_t_s1:minLen_t_s1], '-o', xt_n_s1, tcp_n2_s1[cutOff_t_s1:minLen_t_s1], '-o', xt_n_s1, tcp_n3_s1[cutOff_t_s1:minLen_t_s1], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (10pkts/sec)')
plt.show()
### TCP (faster scenario) n -> s
tcp_n1_s2 = f.getInterPacketArrival(tcp[0][1])
tcp_n2_s2 = f.getInterPacketArrival(tcp[1][1])
tcp_n3_s2 = f.getInterPacketArrival(tcp[2][1])

mean_tcp_n1_s2 = np.mean(tcp_n1_s2)
mean_tcp_n2_s2 = np.mean(tcp_n2_s2)
mean_tcp_n3_s2 = np.mean(tcp_n3_s2)

print("tcp (faster scn) -> n -> s ", mean_tcp_n1_s2, mean_tcp_n2_s2, mean_tcp_n3_s2) 
print("tcp (faster scn) -> n -> s (min, max) ", (np.min(tcp_n1_s2), np.max(tcp_n1_s2)), (np.min(tcp_n2_s2), np.max(tcp_n2_s2)), (np.min(tcp_n3_s2), np.max(tcp_n3_s2)))
print("")
minLen_t_s2 = np.min([ len(tcp_n1_s2), len(tcp_n2_s2), len(tcp_n3_s2) ])

xt_n_s2 = np.linspace(1, minLen_t_s2, minLen_t_s2)

plt.figure()
plt.plot(xt_n_s2, tcp_n1_s2[:minLen_t_s2], '-o', xt_n_s2, tcp_n2_s2[:minLen_t_s2], '-o', xt_n_s2, tcp_n3_s2[:minLen_t_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (100pkts/sec)')
plt.show()

### TCP (Random scenario) n -> s
tcp_n1_s3 = f.getInterPacketArrival(tcp[0][2])
tcp_n2_s3 = f.getInterPacketArrival(tcp[1][2])
tcp_n3_s3 = f.getInterPacketArrival(tcp[2][2])

mean_tcp_n1_s3 = np.mean(tcp_n1_s3)
mean_tcp_n2_s3 = np.mean(tcp_n2_s3)
mean_tcp_n3_s3 = np.mean(tcp_n3_s3)

print("tcp (random scn) -> n -> s ", mean_tcp_n1_s3, mean_tcp_n2_s3, mean_tcp_n3_s3) 
print("tcp (random scn) -> n -> s (min, max) ", (np.min(tcp_n1_s3), np.max(tcp_n1_s3)), (np.min(tcp_n2_s3), np.max(tcp_n2_s3)), (np.min(tcp_n3_s3), np.max(tcp_n3_s3)))
print("")
minLen_t_s3 = np.min([ len(tcp_n1_s3), len(tcp_n2_s3), len(tcp_n3_s3) ])

xt_n_s3 = np.linspace(1, minLen_t_s3, minLen_t_s3)

plt.figure()
plt.plot(xt_n_s3, tcp_n1_s3[:minLen_t_s3], '-o', xt_n_s3, tcp_n2_s3[:minLen_t_s3], '-o', xt_n_s3, tcp_n3_s3[:minLen_t_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for TCP Flood Attack (Random - AFAP)')
plt.show()

## tcp (mean ipat)
plt.figure()
plt.plot(mean_x, [mean_tcp_n1_s1, mean_tcp_n2_s1, mean_tcp_n3_s1], '-o', mean_x, [mean_tcp_n1_s2, mean_tcp_n2_s2, mean_tcp_n3_s2], '-o', mean_x, [mean_tcp_n1_s3, mean_tcp_n2_s3, mean_tcp_n3_s3], '-o')
plt.xlabel('Scenarios')
plt.ylabel('Average Inter-Packet Arrival Time (s)')
plt.title('Average Inter-Packet Arrival Time for TCP Flood Attack')
plt.legend(cpuLegend)
plt.show()

## UDP Inter-Packet Arrival Time
### UDP (fast scenario) n -> s
udp_n1_s1 = f.getInterPacketArrival(udp[0][0])
udp_n2_s1 = f.getInterPacketArrival(udp[1][0])
udp_n3_s1 = f.getInterPacketArrival(udp[2][0])

mean_udp_n1_s1 = np.mean(udp_n1_s1)
mean_udp_n2_s1 = np.mean(udp_n2_s1)
mean_udp_n3_s1 = np.mean(udp_n3_s1)

print("udp (fast scn) -> n -> s ", mean_udp_n1_s1, mean_udp_n2_s1, mean_udp_n3_s1) 
print("udp (fast scn) -> n -> s (min, max) ", (np.min(udp_n1_s1), np.max(udp_n1_s1)), (np.min(udp_n2_s1), np.max(udp_n2_s1)), (np.min(udp_n3_s1), np.max(udp_n3_s1)))
print("")
# remove outliers
udp_n1_s1 = f.trimOutliers(udp_n1_s1, 2)
udp_n2_s1 = f.trimOutliers(udp_n2_s1, 2)
udp_n3_s1 = f.trimOutliers(udp_n3_s1, 3)

minLen_u_s1 = np.min([ len(udp_n1_s1), len(udp_n2_s1), len(udp_n3_s1) ])

xu_n_s1 = np.linspace(1, minLen_u_s1, minLen_u_s1)

plt.figure()
plt.plot(xu_n_s1, udp_n1_s1[:minLen_u_s1], '-o', xu_n_s1, udp_n2_s1[:minLen_u_s1], '-o', xu_n_s1, udp_n3_s1[:minLen_u_s1], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for UDP Flood Attack (10pkts/sec)')
plt.show()

### UDP (faster scenario) n -> s
udp_n1_s2 = f.getInterPacketArrival(udp[0][1])
udp_n2_s2 = f.getInterPacketArrival(udp[1][1])
udp_n3_s2 = f.getInterPacketArrival(udp[2][1])

mean_udp_n1_s2 = np.mean(udp_n1_s2)
mean_udp_n2_s2 = np.mean(udp_n2_s2)
mean_udp_n3_s2 = np.mean(udp_n3_s2)

print("udp (faster scn) -> n -> s ", mean_udp_n1_s2, mean_udp_n2_s2, mean_udp_n3_s2) 
print("udp (faster scn) -> n -> s (min, max) ", (np.min(udp_n1_s2), np.max(udp_n1_s2)), (np.min(udp_n2_s2), np.max(udp_n2_s2)), (np.min(udp_n3_s2), np.max(udp_n3_s2)))
print("")
minLen_u_s2 = np.min([ len(udp_n1_s2), len(udp_n2_s2), len(udp_n3_s2) ])

xu_n_s2 = np.linspace(1, minLen_u_s2, minLen_u_s2)

plt.figure()
plt.plot(xu_n_s2, udp_n1_s2[:minLen_u_s2], '-o', xu_n_s2, udp_n2_s2[:minLen_u_s2], '-o', xu_n_s2, udp_n3_s2[:minLen_u_s2], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival Time for UDP Flood Attack (100pkts/sec)') 
plt.show()

### UDP (Random - AFAP) n -> s
udp_n1_s3 = f.getInterPacketArrival(udp[0][2])
udp_n2_s3 = f.getInterPacketArrival(udp[1][2])
udp_n3_s3 = f.getInterPacketArrival(udp[2][2])

mean_udp_n1_s3 = np.mean(udp_n1_s3)
mean_udp_n2_s3 = np.mean(udp_n2_s3)
mean_udp_n3_s3 = np.mean(udp_n3_s3)

print("udp (random scn) -> n -> s ", mean_udp_n1_s3, mean_udp_n2_s3, mean_udp_n3_s3) 
print("udp (random scn) -> n -> s (min, max) ", (np.min(udp_n1_s3), np.max(udp_n1_s3)), (np.min(udp_n2_s3), np.max(udp_n2_s3)), (np.min(udp_n3_s3), np.max(udp_n3_s3)))
print("")
# removing outliers
udp_n1_s3 = f.trimOutliers(udp_n1_s3, 1)
udp_n2_s3 = f.trimOutliers(udp_n2_s3, 2)
udp_n3_s3 = f.trimOutliers(udp_n3_s3, 1)

minLen_u_s3 = np.min([ len(udp_n1_s3), len(udp_n2_s3), len(udp_n3_s3) ])

xu_n_s3 = np.linspace(1, minLen_u_s3, minLen_u_s3)

plt.figure()
plt.plot(xu_n_s3, udp_n1_s3[:minLen_u_s3], '-o', xu_n_s3, udp_n2_s3[:minLen_u_s3], '-o', xu_n_s3, udp_n3_s3[:minLen_u_s3], '-o')
plt.xlabel('Packets')
plt.ylabel('Inter-Packet Arrival Time (s)')
plt.legend(nodesLegend)
plt.title('Inter-Packet Arrival time for UDP Flood Attack (Random - AFAP)')
plt.show()

## udp (mean ipat)
plt.figure()
plt.plot(mean_x, [mean_udp_n1_s1, mean_udp_n2_s1, mean_udp_n3_s1], '-o', mean_x, [mean_udp_n1_s2, mean_udp_n2_s2, mean_udp_n3_s2], '-o', mean_x, [mean_udp_n1_s3, mean_udp_n2_s3, mean_udp_n3_s3], '-o')
plt.xlabel('Scenarios')
plt.ylabel('Average Inter-Packet Arrival Time (s)')
plt.title('Average Inter-Packet Arrival Time for UDP Flood Attack')
plt.legend(cpuLegend)
plt.show()

"""
## Checking the effect of the DoS on CPU

icmpCPU = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
tcpCPU  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
udpCPU  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]

minLenCPU = 200

for x in scenarios:
    # icmp
    for data in db.getPS("icmp", x):
        node = data['node']
        scn = data['scenario']
        icmpCPU[node - 1][scn - 1].append(data['cpu_percent'])

    # tcp
    for data in db.getPS("tcp", x):
        node = data['node']
        scn = data['scenario']
        tcpCPU[node -1 ][scn - 1].append(data['cpu_percent'])

    # udp
    for data in db.getPS("udp", x):
        node = data['node']
        scn = data['scenario']
        udpCPU[node - 1][scn - 1].append(data['cpu_percent'])

## icmp -> cpu -> s1
icmpCPU_s1_n1 = icmpCPU[0][0]
icmpCPU_s1_n2 = icmpCPU[1][0]
icmpCPU_s1_n3 = icmpCPU[2][0]
cpuLegend3 = ['N1_Attack', 'N2_Attack', 'N3_Attack', 'N1_Normal', 'N2_Normal', 'N3_Normal']
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpCPU_s1_n1[:minLenCPU], '-o', x, icmpCPU_s1_n2[:minLenCPU], '-o', x, icmpCPU_s1_n3[:minLenCPU], '-o', x, cpuData_n1[0][:minLenCPU], '-o', x, cpuData_n2[0][:minLenCPU], '-o', x, cpuData_n3[0][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (ICMP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> cpu -> s2
icmpCPU_s2_n1 = icmpCPU[0][1]
icmpCPU_s2_n2 = icmpCPU[1][1]
icmpCPU_s2_n3 = icmpCPU[2][1]

plt.figure()
plt.plot(x, icmpCPU_s2_n1[:minLenCPU], '-o', x, icmpCPU_s2_n2[:minLenCPU], '-o', x, icmpCPU_s2_n3[:minLenCPU], '-o', x, cpuData_n1[1][:minLenCPU], '-o', x, cpuData_n2[1][:minLenCPU], '-o', x, cpuData_n3[1][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (ICMP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> cpu -> s3
icmpCPU_s3_n1 = icmpCPU[0][2]
icmpCPU_s3_n2 = icmpCPU[1][2]
icmpCPU_s3_n3 = icmpCPU[2][2]

plt.figure()
plt.plot(x, icmpCPU_s3_n1[:minLenCPU], '-o', x, icmpCPU_s3_n2[:minLenCPU], '-o', x, icmpCPU_s3_n3[:minLenCPU], '-o', x, cpuData_n1[2][:minLenCPU], '-o', x, cpuData_n2[2][:minLenCPU], '-o', x, cpuData_n3[2][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode \n(ICMP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cpu -> s1
tcpCPU_s1_n1 = tcpCPU[0][0]
tcpCPU_s1_n2 = tcpCPU[1][0]
tcpCPU_s1_n3 = tcpCPU[2][0]

plt.figure()
plt.plot(x, tcpCPU_s1_n1[:minLenCPU], '-o', x, tcpCPU_s1_n2[:minLenCPU], '-o', x, tcpCPU_s1_n3[:minLenCPU], '-o', x, cpuData_n1[0][:minLenCPU], '-o', x, cpuData_n2[0][:minLenCPU], '-o', x, cpuData_n3[0][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (TCP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cpu -> s2
tcpCPU_s2_n1 = tcpCPU[0][1]
tcpCPU_s2_n2 = tcpCPU[1][1]
tcpCPU_s2_n3 = tcpCPU[2][1]

plt.figure()
plt.plot(x, tcpCPU_s2_n1[:minLenCPU], '-o', x, tcpCPU_s2_n2[:minLenCPU], '-o', x, tcpCPU_s2_n3[:minLenCPU], '-o', x, cpuData_n1[1][:minLenCPU], '-o', x, cpuData_n2[1][:minLenCPU], '-o', x, cpuData_n3[1][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (TCP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cpu -> s3
tcpCPU_s3_n1 = tcpCPU[0][2]
tcpCPU_s3_n2 = tcpCPU[1][2]
tcpCPU_s3_n3 = tcpCPU[2][2]

plt.figure()
plt.plot(x, tcpCPU_s3_n1[:minLenCPU], '-o', x, tcpCPU_s3_n2[:minLenCPU], '-o', x, tcpCPU_s3_n3[:minLenCPU], '-o', x, cpuData_n1[2][:minLenCPU], '-o', x, cpuData_n2[2][:minLenCPU], '-o', x, cpuData_n3[2][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode \n(TCP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cpu -> s1
udpCPU_s1_n1 = udpCPU[0][0]
udpCPU_s1_n2 = udpCPU[1][0]
udpCPU_s1_n3 = udpCPU[2][0]

plt.figure()
plt.plot(x, udpCPU_s1_n1[:minLenCPU], '-o', x, udpCPU_s1_n2[:minLenCPU], '-o', x, udpCPU_s1_n3[:minLenCPU], '-o', x, cpuData_n1[0][:minLenCPU], '-o', x, cpuData_n2[0][:minLenCPU], '-o', x, cpuData_n3[0][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (UDP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cpu -> s2
udpCPU_s2_n1 = udpCPU[0][1]
udpCPU_s2_n2 = udpCPU[1][1]
udpCPU_s2_n3 = udpCPU[2][1]

plt.figure()
plt.plot(x, udpCPU_s2_n1[:minLenCPU], '-o', x, udpCPU_s2_n2[:minLenCPU], '-o', x, udpCPU_s2_n3[:minLenCPU], '-o', x, cpuData_n1[1][:minLenCPU], '-o', x, cpuData_n2[1][:minLenCPU], '-o', x, cpuData_n3[1][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode (UDP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cpu -> s3
udpCPU_s3_n1 = udpCPU[0][2]
udpCPU_s3_n2 = udpCPU[1][2]
udpCPU_s3_n3 = udpCPU[2][2]

plt.figure()
plt.plot(x, udpCPU_s3_n1[:minLenCPU], '-o', x, udpCPU_s3_n2[:minLenCPU], '-o', x, udpCPU_s3_n3[:minLenCPU], '-o', x, cpuData_n1[2][:minLenCPU], '-o', x, cpuData_n2[2][:minLenCPU], '-o', x, cpuData_n3[2][:minLenCPU], '-o')
plt.ylabel('CPU Utilization (%)')
plt.xlabel('Number of Times')
plt.title('CPU Utilization of nodes in normal and attack mode \n(UDP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## Memory Utilization
memData= [[[], [], []], [[], [], []], [[], [], []]] # n1, n2, n3

for scenario in range(1, 4):
    for node in range(1, 4):
        for data in db.getCPUData(node, scenario):
            n = node - 1
            scn = scenario - 1
            memData[n][scn].append(data['mem_p'])


## Checking the effect of the DoS on Memory
icmpMem = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
tcpMem  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
udpMem  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]

minLenCPU = 200

for x in scenarios:
    # icmp
    for data in db.getPS("icmp", x):
        node = data['node']
        scn = data['scenario']
        icmpMem[node - 1][scn - 1].append(data['mem_p'])

    # tcp
    for data in db.getPS("tcp", x):
        node = data['node']
        scn = data['scenario']
        tcpMem[node -1 ][scn - 1].append(data['mem_p'])

    # udp
    for data in db.getPS("udp", x):
        node = data['node']
        scn = data['scenario']
        udpMem[node - 1][scn - 1].append(data['mem_p'])

## icmp -> mem -> s1
icmpMem_s1_n1 = icmpMem[0][0]
icmpMem_s1_n2 = icmpMem[1][0]
icmpMem_s1_n3 = icmpMem[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpMem_s1_n1[:minLenCPU], '-o', x, icmpMem_s1_n2[:minLenCPU], '-o', x, icmpMem_s1_n3[:minLenCPU], '-o', x, memData[0][0][:minLenCPU], '-o', x, memData[1][0][:minLenCPU], '-o', x, memData[2][0][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (ICMP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> mem -> s2
icmpMem_s2_n1 = icmpMem[0][1]
icmpMem_s2_n2 = icmpMem[1][1]
icmpMem_s2_n3 = icmpMem[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpMem_s2_n1[:minLenCPU], '-o', x, icmpMem_s2_n2[:minLenCPU], '-o', x, icmpMem_s2_n3[:minLenCPU], '-o', x, memData[0][1][:minLenCPU], '-o', x, memData[1][1][:minLenCPU], '-o', x, memData[2][1][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (ICMP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> mem -> s3
icmpMem_s3_n1 = icmpMem[0][2]
icmpMem_s3_n2 = icmpMem[1][2]
icmpMem_s3_n3 = icmpMem[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpMem_s3_n1[:minLenCPU], '-o', x, icmpMem_s3_n2[:minLenCPU], '-o', x, icmpMem_s3_n3[:minLenCPU], '-o', x, memData[0][2][:minLenCPU], '-o', x, memData[1][2][:minLenCPU], '-o', x, memData[2][2][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (ICMP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> mem -> s1
tcpMem_s1_n1 = tcpMem[0][0]
tcpMem_s1_n2 = tcpMem[1][0]
tcpMem_s1_n3 = tcpMem[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpMem_s1_n1[:minLenCPU], '-o', x, tcpMem_s1_n2[:minLenCPU], '-o', x, tcpMem_s1_n3[:minLenCPU], '-o', x, memData[0][0][:minLenCPU], '-o', x, memData[1][0][:minLenCPU], '-o', x, memData[2][0][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (TCP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> mem -> s2
tcpMem_s2_n1 = tcpMem[0][1]
tcpMem_s2_n2 = tcpMem[1][1]
tcpMem_s2_n3 = tcpMem[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpMem_s2_n1[:minLenCPU], '-o', x, tcpMem_s2_n2[:minLenCPU], '-o', x, tcpMem_s2_n3[:minLenCPU], '-o', x, memData[0][1][:minLenCPU], '-o', x, memData[1][1][:minLenCPU], '-o', x, memData[2][1][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (TCP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> mem -> s3
tcpMem_s3_n1 = tcpMem[0][2]
tcpMem_s3_n2 = tcpMem[1][2]
tcpMem_s3_n3 = tcpMem[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpMem_s3_n1[:minLenCPU], '-o', x, tcpMem_s3_n2[:minLenCPU], '-o', x, tcpMem_s3_n3[:minLenCPU], '-o', x, memData[0][2][:minLenCPU], '-o', x, memData[1][2][:minLenCPU], '-o', x, memData[2][2][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (TCP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## udp -> mem -> s1
udpMem_s1_n1 = udpMem[0][0]
udpMem_s1_n2 = udpMem[1][0]
udpMem_s1_n3 = udpMem[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpMem_s1_n1[:minLenCPU], '-o', x, udpMem_s1_n2[:minLenCPU], '-o', x, udpMem_s1_n3[:minLenCPU], '-o', x, memData[0][0][:minLenCPU], '-o', x, memData[1][0][:minLenCPU], '-o', x, memData[2][0][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (UDP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> mem -> s2
udpMem_s2_n1 = udpMem[0][1]
udpMem_s2_n2 = udpMem[1][1]
udpMem_s2_n3 = udpMem[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpMem_s2_n1[:minLenCPU], '-o', x, udpMem_s2_n2[:minLenCPU], '-o', x, udpMem_s2_n3[:minLenCPU], '-o', x, memData[0][1][:minLenCPU], '-o', x, memData[1][1][:minLenCPU], '-o', x, memData[2][1][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (UDP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> mem -> s3
udpMem_s3_n1 = udpMem[0][2]
udpMem_s3_n2 = udpMem[1][2]
udpMem_s3_n3 = udpMem[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpMem_s3_n1[:minLenCPU], '-o', x, udpMem_s3_n2[:minLenCPU], '-o', x, udpMem_s3_n3[:minLenCPU], '-o', x, memData[0][2][:minLenCPU], '-o', x, memData[1][2][:minLenCPU], '-o', x, memData[2][2][:minLenCPU], '-o')
plt.ylabel('Memory Utilization (%)')
plt.xlabel('Number of Times')
plt.title('Memory Utilization of nodes in normal and attack mode\n (UDP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()


## Checking the effect of the DoS on ctx_switches
csData= [[[], [], []], [[], [], []], [[], [], []]] # n1, n2, n3

for scenario in range(1, 4):
    for node in range(1, 4):
        for data in db.getCPUData(node, scenario):
            n = node - 1
            scn = scenario - 1
            csData[n][scn].append(data['ctx_switches'])

icmpCs = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
tcpCs  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
udpCs  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]

minLenCPU = 200

for x in scenarios:
    # icmp
    for data in db.getPS("icmp", x):
        node = data['node']
        scn = data['scenario']
        icmpCs[node - 1][scn - 1].append(data['ctx_switches'])

    # tcp
    for data in db.getPS("tcp", x):
        node = data['node']
        scn = data['scenario']
        tcpCs[node -1 ][scn - 1].append(data['ctx_switches'])

    # udp
    for data in db.getPS("udp", x):
        node = data['node']
        scn = data['scenario']
        udpCs[node - 1][scn - 1].append(data['ctx_switches'])

## icmp -> cs -> s1
icmpCs_s1_n1 = icmpCs[0][0]
icmpCs_s1_n2 = icmpCs[1][0]
icmpCs_s1_n3 = icmpCs[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpCs_s1_n1[:minLenCPU], '-o', x, icmpCs_s1_n2[:minLenCPU], '-o', x, icmpCs_s1_n3[:minLenCPU], '-o', x, csData[0][0][:minLenCPU], '-o', x, csData[1][0][:minLenCPU], '-o', x, csData[2][0][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (ICMP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> cs -> s2
icmpCs_s2_n1 = icmpCs[0][1]
icmpCs_s2_n2 = icmpCs[1][1]
icmpCs_s2_n3 = icmpCs[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpCs_s2_n1[:minLenCPU], '-o', x, icmpCs_s2_n2[:minLenCPU], '-o', x, icmpCs_s2_n3[:minLenCPU], '-o', x, csData[0][1][:minLenCPU], '-o', x, csData[1][1][:minLenCPU], '-o', x, csData[2][1][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (ICMP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> cs -> s3
icmpCs_s3_n1 = icmpCs[0][2]
icmpCs_s3_n2 = icmpCs[1][2]
icmpCs_s3_n3 = icmpCs[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpCs_s3_n1[:minLenCPU], '-o', x, icmpCs_s3_n2[:minLenCPU], '-o', x, icmpCs_s3_n3[:minLenCPU], '-o', x, csData[0][2][:minLenCPU], '-o', x, csData[1][2][:minLenCPU], '-o', x, csData[2][2][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (ICMP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cs -> s1
tcpCs_s1_n1 = tcpCs[0][0]
tcpCs_s1_n2 = tcpCs[1][0]
tcpCs_s1_n3 = tcpCs[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpCs_s1_n1[:minLenCPU], '-o', x, tcpCs_s1_n2[:minLenCPU], '-o', x, tcpCs_s1_n3[:minLenCPU], '-o', x, csData[0][0][:minLenCPU], '-o', x, csData[1][0][:minLenCPU], '-o', x, csData[2][0][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (TCP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cs -> s2
tcpCs_s2_n1 = tcpCs[0][1]
tcpCs_s2_n2 = tcpCs[1][1]
tcpCs_s2_n3 = tcpCs[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpCs_s2_n1[:minLenCPU], '-o', x, tcpCs_s2_n2[:minLenCPU], '-o', x, tcpCs_s2_n3[:minLenCPU], '-o', x, csData[0][1][:minLenCPU], '-o', x, csData[1][1][:minLenCPU], '-o', x, csData[2][1][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (TCP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> cs -> s3
tcpCs_s3_n1 = tcpCs[0][2]
tcpCs_s3_n2 = tcpCs[1][2]
tcpCs_s3_n3 = tcpCs[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpCs_s3_n1[:minLenCPU], '-o', x, tcpCs_s3_n2[:minLenCPU], '-o', x, tcpCs_s3_n3[:minLenCPU], '-o', x, csData[0][2][:minLenCPU], '-o', x, csData[1][2][:minLenCPU], '-o', x, csData[2][2][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (TCP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cs -> s1
udpCs_s1_n1 = udpCs[0][0]
udpCs_s1_n2 = udpCs[1][0]
udpCs_s1_n3 = udpCs[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpCs_s1_n1[:minLenCPU], '-o', x, udpCs_s1_n2[:minLenCPU], '-o', x, udpCs_s1_n3[:minLenCPU], '-o', x, csData[0][0][:minLenCPU], '-o', x, csData[1][0][:minLenCPU], '-o', x, csData[2][0][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (UDP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cs -> s2
udpCs_s2_n1 = udpCs[0][1]
udpCs_s2_n2 = udpCs[1][1]
udpCs_s2_n3 = udpCs[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpCs_s2_n1[:minLenCPU], '-o', x, udpCs_s2_n2[:minLenCPU], '-o', x, udpCs_s2_n3[:minLenCPU], '-o', x, csData[0][1][:minLenCPU], '-o', x, csData[1][1][:minLenCPU], '-o', x, csData[2][1][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (UDP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> cs -> s3
udpCs_s3_n1 = udpCs[0][2]
udpCs_s3_n2 = udpCs[1][2]
udpCs_s3_n3 = udpCs[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpCs_s3_n1[:minLenCPU], '-o', x, udpCs_s3_n2[:minLenCPU], '-o', x, udpCs_s3_n3[:minLenCPU], '-o', x, csData[0][2][:minLenCPU], '-o', x, csData[1][2][:minLenCPU], '-o', x, csData[2][2][:minLenCPU], '-o')
plt.ylabel('Context Switches')
plt.xlabel('Number of Times')
plt.title('Context Switches of nodes in normal and attack mode\n (UDP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()


## Checking the effect of the DoS on soft_interrupts
siData= [[[], [], []], [[], [], []], [[], [], []]] # n1, n2, n3

for scenario in range(1, 4):
    for node in range(1, 4):
        for data in db.getCPUData(node, scenario):
            n = node - 1
            scn = scenario - 1
            siData[n][scn].append(data['soft_interrupts'])

icmpSi = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
tcpSi  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]
udpSi  = [ [[], [], []],  [[], [], []], [[], [], []] ] # node [s1, s2, s3]

minLenCPU = 200

for x in scenarios:
    # icmp
    for data in db.getPS("icmp", x):
        node = data['node']
        scn = data['scenario']
        icmpSi[node - 1][scn - 1].append(data['soft_interrupts'])

    # tcp
    for data in db.getPS("tcp", x):
        node = data['node']
        scn = data['scenario']
        tcpSi[node -1 ][scn - 1].append(data['soft_interrupts'])

    # udp
    for data in db.getPS("udp", x):
        node = data['node']
        scn = data['scenario']
        udpSi[node - 1][scn - 1].append(data['soft_interrupts'])

## icmp -> si -> s1
icmpSi_s1_n1 = icmpSi[0][0]
icmpSi_s1_n2 = icmpSi[1][0]
icmpSi_s1_n3 = icmpSi[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpSi_s1_n1[:minLenCPU], '-o', x, icmpSi_s1_n2[:minLenCPU], '-o', x, icmpSi_s1_n3[:minLenCPU], '-o', x, siData[0][0][:minLenCPU], '-o', x, siData[1][0][:minLenCPU], '-o', x, siData[2][0][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (ICMP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> si -> s2
icmpSi_s2_n1 = icmpSi[0][1]
icmpSi_s2_n2 = icmpSi[1][1]
icmpSi_s2_n3 = icmpSi[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpSi_s2_n1[:minLenCPU], '-o', x, icmpSi_s2_n2[:minLenCPU], '-o', x, icmpSi_s2_n3[:minLenCPU], '-o', x, siData[0][1][:minLenCPU], '-o', x, siData[1][1][:minLenCPU], '-o', x, siData[2][1][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (ICMP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## icmp -> si -> s3
icmpSi_s3_n1 = icmpSi[0][2]
icmpSi_s3_n2 = icmpSi[1][2]
icmpSi_s3_n3 = icmpSi[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, icmpSi_s3_n1[:minLenCPU], '-o', x, icmpSi_s3_n2[:minLenCPU], '-o', x, icmpSi_s3_n3[:minLenCPU], '-o', x, siData[0][2][:minLenCPU], '-o', x, siData[1][2][:minLenCPU], '-o', x, siData[2][2][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (ICMP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> si -> s1
tcpSi_s1_n1 = tcpSi[0][0]
tcpSi_s1_n2 = tcpSi[1][0]
tcpSi_s1_n3 = tcpSi[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpSi_s1_n1[:minLenCPU], '-o', x, tcpSi_s1_n2[:minLenCPU], '-o', x, tcpSi_s1_n3[:minLenCPU], '-o', x, siData[0][0][:minLenCPU], '-o', x, siData[1][0][:minLenCPU], '-o', x, siData[2][0][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (TCP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> si -> s2
tcpSi_s2_n1 = tcpSi[0][1]
tcpSi_s2_n2 = tcpSi[1][1]
tcpSi_s2_n3 = tcpSi[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpSi_s2_n1[:minLenCPU], '-o', x, tcpSi_s2_n2[:minLenCPU], '-o', x, tcpSi_s2_n3[:minLenCPU], '-o', x, siData[0][1][:minLenCPU], '-o', x, siData[1][1][:minLenCPU], '-o', x, siData[2][1][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (TCP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## tcp -> si -> s3
tcpSi_s3_n1 = tcpSi[0][2]
tcpSi_s3_n2 = tcpSi[1][2]
tcpSi_s3_n3 = tcpSi[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, tcpSi_s3_n1[:minLenCPU], '-o', x, tcpSi_s3_n2[:minLenCPU], '-o', x, tcpSi_s3_n3[:minLenCPU], '-o', x, siData[0][2][:minLenCPU], '-o', x, siData[1][2][:minLenCPU], '-o', x, siData[2][2][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (TCP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()

## udp -> si -> s1
udpSi_s1_n1 = udpSi[0][0]
udpSi_s1_n2 = udpSi[1][0]
udpSi_s1_n3 = udpSi[2][0]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpSi_s1_n1[:minLenCPU], '-o', x, udpSi_s1_n2[:minLenCPU], '-o', x, udpSi_s1_n3[:minLenCPU], '-o', x, siData[0][0][:minLenCPU], '-o', x, siData[1][0][:minLenCPU], '-o', x, siData[2][0][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (UDP Flood: 10pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> si -> s2
udpSi_s2_n1 = udpSi[0][1]
udpSi_s2_n2 = udpSi[1][1]
udpSi_s2_n3 = udpSi[2][1]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpSi_s2_n1[:minLenCPU], '-o', x, udpSi_s2_n2[:minLenCPU], '-o', x, udpSi_s2_n3[:minLenCPU], '-o', x, siData[0][1][:minLenCPU], '-o', x, siData[1][1][:minLenCPU], '-o', x, siData[2][1][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (UDP Flood: 100pkt/s)')
plt.legend(cpuLegend3)
plt.show()

## udp -> si -> s3
udpSi_s3_n1 = udpSi[0][2]
udpSi_s3_n2 = udpSi[1][2]
udpSi_s3_n3 = udpSi[2][2]
x = np.linspace(1, minLenCPU, minLenCPU)

plt.figure()
plt.plot(x, udpSi_s3_n1[:minLenCPU], '-o', x, udpSi_s3_n2[:minLenCPU], '-o', x, udpSi_s3_n3[:minLenCPU], '-o', x, siData[0][2][:minLenCPU], '-o', x, siData[1][2][:minLenCPU], '-o', x, siData[2][2][:minLenCPU], '-o')
plt.ylabel('Soft Interrupts')
plt.xlabel('Number of Times')
plt.title('Soft Interrupts of nodes in normal and attack mode\n (UDP Flood: Random - AFAP)')
plt.legend(cpuLegend3)
plt.show()
"""
