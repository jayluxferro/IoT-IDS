#!/usr/bin/python

import matplotlib.pyplot as plt
import db

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


