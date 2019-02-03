#!/usr/bin/python

import matplotlib.pyplot as plt
import pymongo

dbClient = pymongo.MongoClient("mongodb://localhost:27017/siem")
db = dbClient["siem"]

single = db["single"]

x = [] # number of APs detected
y = [] # execution time


#data = single.find({})
for a in single.find({}):
    x.append(a['memory'])
    y.append(a['exec'])

#print(x)
#print(y)

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
plt.ylabel('Exection Time(seconds)')
plt.show()


