#!/usr/bin/python

import db
import matplotlib.pyplot as plt
import func
import numpy as np

scenarios = 50
min_val = 0
max_val = 1000
collisions = []
collisions_buffer = []
collisions_cpu = []
collisions_buffer_cpu = []
collisions_time = []
collisions_buffer_time = []

x = np.linspace(0, scenarios, scenarios + 1)[1:]

for s in range(scenarios):
    collisions.append(func.getCollisionsSum("collisions", min_val, max_val, s + 1))

    collisions_buffer.append(func.getCollisionsSum("collisions_buffer", min_val, max_val, s + 1))
    
    collisions_cpu.append(func.getAvg("percent", "wh", min_val, max_val, s + 1))

    collisions_buffer_cpu.append(func.getAvg("percent", "wh_buffer", min_val, max_val, s + 1))

    collisions_time.append(func.getAvg("time", "wh", min_val, max_val, s + 1))

    collisions_buffer_time.append(func.getAvg("time", "wh_buffer", min_val, max_val, s + 1))


# Collisions
plt.figure(1)
plt.plot(x, collisions, '-o', label='No buffer')
plt.plot(x, collisions_buffer, '-o', label='Buffer')
plt.legend()
plt.xlabel('Scenarios')
plt.ylabel('Number of collisions detected')
plt.grid(axis='both')
plt.title('Graph showing the number of collisions detected\n using Wichmann-Hill pseudorandom number generator\n(1000 iterations)')
plt.show()

print("Collision Default avg: " + str(np.average(collisions)))
print("Collision Buffer avg: " + str(np.average(collisions_buffer)))



# CPU usage
plt.figure(2)
plt.plot(x, collisions_cpu, '-o', label='No buffer')
plt.plot(x, collisions_buffer_cpu, '-o', label='Buffer')
plt.legend()
plt.xlabel('Scenarios')
plt.ylabel('CPU utilization (%)')
plt.grid(axis='both')
plt.title('Graph showing the CPU utilization efficiency\n using Wichmann-Hill pseudorandom number generator\n(1000 iterations)')
plt.show()

"""
Average CPU Usage
"""
collisions_cpu_avg = np.average(collisions_cpu)
collisions_buffer_cpu_avg = np.average(collisions_buffer_cpu)

fig, ax = plt.subplots()
ind = np.arange(1, 3)
avg_cpu = [collisions_cpu_avg, collisions_buffer_cpu_avg]

d, b = plt.bar(ind, avg_cpu)
#d.set_facecolor('r')
b.set_facecolor('orange')
ax.set_xticks(ind)
ax.set_xticklabels(['No Buffer', 'Buffer'])
ax.set_ylabel('Average CPU utilization (%)')
ax.set_xlabel('Scenarios')
plt.title('Average CPU utilization efficiency\n using Wichmann-Hill pseudorandom number generator\n(1000 iterations)')
plt.show()
print("Avg CPU: nb/b " + str(avg_cpu))


## Random Number Generation Time(s)
plt.figure(4)
plt.plot(x, collisions_time, '-o', label='No Buffer')
plt.plot(x, collisions_buffer_time, '-o', label='Buffer')
plt.xlabel('Scenarios')
plt.ylabel('Time taken to generate random number (s)')
plt.legend()
plt.grid(axis='both')
plt.show()

"""
Average Random Number Generation Time
"""
time_avg = np.average(collisions_time)
time_buffer_avg = np.average(collisions_buffer_time)

fig, ax = plt.subplots()
ind = np.arange(1, 3)
avg_time = [time_avg, time_buffer_avg]

d, b = plt.bar(ind, avg_time)
b.set_facecolor('orange')
ax.set_xticks(ind)
ax.set_xticklabels(['No Buffer', 'Buffer'])
ax.set_ylabel('Average time taken to generate random number (s)')
ax.set_xlabel('Scenarios')
plt.title('Average Time taken to generate the Wichmann-Hill pseudorandom number\n (1000 iterations)')
plt.show()
print("Avg Time: nb/b " + str(avg_time))

