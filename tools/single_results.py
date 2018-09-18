#!/usr/bin/python3

import matplotlib.pyplot as plt
import pymongo

dbClient = pymongo.MongoClient("mongodb://siem:siem@localhost:27017/siem")
db = dbClient["siem"]

single = db["single"]

x = [] # number of APs detected
y = [] # execution time


#data = single.find({})
for a in single.find({}):
    x.append(a['aps'])
    y.append(a['exec'])

#print(x)
#print(y)
plt.figure(1)
plt.grid(True)
plt.subplot(211)
plt.plot(x, 'r')
plt.ylabel('Number of detected access points')
plt.xlabel('Number of Iterations')

plt.subplot(212)

plt.plot(y)
plt.ylabel('Execution Time (seconds)')
plt.xlabel('Number of Iterations')
plt.show()


