#!/usr/bin/python

import matplotlib.pyplot as plt
import db
import numpy as np

"""
x = [] # memory
y = [] # execution time

conn = db.init()
c = conn.cursor()

for a in c.execute('select * from single'):
    x.append(a[3]) # memory
    y.append(a[2]) # exec


## Figure 1
# Subplot 1
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(y)
plt.ylabel('Execution Time (seconds)')
plt.xlabel('Number of Iterations')
plt.grid(True)

# Subplot 2
plt.subplot(2, 1, 2)
plt.plot(x, 'r')
plt.ylabel('Memory Usage(%)')
plt.xlabel('Number of Iterations')
plt.grid(True)
plt.tight_layout()
plt.show()

## Figure 2
plt.figure(2)
plt.grid(True)
plt.plot(y, '*g')
plt.xlabel('Number of Iterations')
plt.ylabel('Execution Time(seconds)')
plt.show()
"""
con = db.init()

sn1 = []
sn2 = []
sn3 = []

for x in con.cursor().execute("select * from scenarios").fetchall():
    # id, aps, execution_time, usage, entropy, scenario, distance
    # 0,   1     2                3      4           5       6
    if x[5] == 0:
        sn1.append(x)

    elif x[5] == 2:
        sn2.append(x)

    elif x[5] == 3:
        sn3.append(x)


## Scenario 1
# Detection Rate
x1 = []
y1 = []
c1 = []

for s in sn1:
    x1.append(s[6])
    y1.append(s[2])
    c1.append(s[3])

plt.figure(1)
plt.plot(x1, y1, '-o')
plt.ylabel("Detection Rate (s)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the detection rate using Algorithm 1 (Scenario 1)")
plt.show()

# CPU usage
plt.figure(2)
plt.plot(x1, c1, '-ro')
plt.ylabel("CPU Usage (%)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the CPU usage using Algorithm 1 (Scenario 1)")
plt.show()


## Scenario 2
# Detection Rate
x2 = []
y2 = []
c2 = []

for s in sn2:
    x2.append(s[6])
    y2.append(s[2])
    c2.append(s[3])

plt.figure(3)
plt.plot(x2, y2, '-o')
plt.ylabel("Detection Rate (s)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the detection rate using Algorithm 2\n with random channel hopping (Scenario 2)")
plt.show()

# CPU usage
plt.figure(4)
plt.plot(x2, c2, '-ro')
plt.ylabel("CPU Usage (%)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the CPU usage using Algorithm 2\n with random channel hopping (Scenario 2)")
plt.show()



## Scenario 3
# Detection Rate
x3 = []
y3 = []
c3 = []

for s in sn3:
    x3.append(s[6])
    y3.append(s[2])
    c3.append(s[3])

plt.figure(5)
plt.plot(x3, y3, '-o')
plt.ylabel("Detection Rate (s)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the detection rate using Algorithm 2\n with iterative channel hopping (Scenario 3)")
plt.show()

# CPU usage
plt.figure(6)
plt.plot(x3, c3, '-ro')
plt.ylabel("CPU Usage (%)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the CPU usage using Algorithm 2 \nwith iterative channel hopping (Scenario 3)")
plt.show()



# All three scenarios
## Detection Rate
plt.figure(7)
plt.plot(x1, y1, '-o', label='Scenario 1')
plt.plot(x2, y2, '-o', label='Scenario 2')
plt.plot(x3, y3, '-o', label='Scenario 3')
plt.legend()
plt.ylabel("Detection Rate (s)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the comparison of the detection rate\n in all three scenarios")
plt.show()


## CPU Usage
plt.figure(8)
plt.plot(x1, c1, '-o', label='Scenario 1')
plt.plot(x2, c2, '-o', label='Scenario 2')
plt.plot(x3, c3, '-o', label='Scenario 3')
plt.legend()
plt.ylabel("CPU usage (%)")
plt.grid(axis='both')
plt.xlabel("Distance between legitimate AP and rogue AP (m)")
#plt.title("Graph showing the comparison of the CPU usage\n in all three scenarios")
plt.show()


x1Avg = 0
x2Avg = 0
x3Avg = 0
c1Avg = 0
c2Avg = 0
c3Avg = 0

for x in sn1:
    # id, aps, execution_time, usage, entropy, scenario, distance
    # 0,   1     2
    x1Avg = x1Avg + x[2]
    c1Avg = c1Avg + x[3]
x1Avg = x1Avg/len(x1)
c1Avg = c1Avg/len(x1)

for x in sn2:
    # id, aps, execution_time, usage, entropy, scenario, distance
    # 0,   1     2
    x2Avg = x2Avg + x[2]
    c2Avg = c2Avg + x[3]
x2Avg = x2Avg/len(x2)
c2Avg = c2Avg/len(x2)


for x in sn3:
    # id, aps, execution_time, usage, entropy, scenario, distance
    # 0,   1     2
    x3Avg = x3Avg + x[2]
    c3Avg = c3Avg + x[3]
x3Avg = x3Avg/len(x3)
c3Avg = c3Avg/len(x3)

index = np.arange(3)
bar_width = 0.35

opacity = 0.7
rate = (x1Avg, x2Avg, x3Avg)
cpu = (c1Avg, c2Avg, c3Avg)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Scenarios')
ax1.set_ylabel('Detection Rate (s)', color=color)
ax1.bar(index, rate, bar_width, alpha=opacity, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('CPU Usage (%)', color=color)
ax2.bar(index + 0.35, cpu, bar_width, alpha=opacity, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_xticklabels(('', '  Scenario 1', '', 'Scenario 2', '', 'Scenario 3', '', '', ''))
# fig.tight_layout()
#plt.title("Comparison of the average detection rate \nand CPU usage of all three scenarios")
plt.grid(axis='both')
plt.show()

# display averages
print(rate)
print(cpu)