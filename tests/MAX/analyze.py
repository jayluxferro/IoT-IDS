#!/usr/bin/python

import db
import matplotlib.pyplot as plt
import func

"""
collisions = []
detections = []

for x in db.getCollisions():
    collisions.append({'counter': x[1], 'collisions': x[2], 'scenario': x[3]})

for i in db.getDetections():
    detections.append({'counter': x[1], 'collisions': x[2], 'scenario': x[3]})
"""

collisions = [0, 0, 0]
detections = [0, 0, 0]

collisions[0] = func.getCollisionsSum(0, 1000, 1)
collisions[1] = func.getCollisionsSum(0, 1000, 2)
collisions[2] = func.getCollisionsSum(0, 1000, 3)


detections[0] = func.getDetectionsAvg(0, 1000, 1)
detections[1] = func.getDetectionsAvg(0, 1000, 2)
detections[2] = func.getDetectionsAvg(0, 1000, 3)

x = [1, 2, 3]

# Collisions
plt.figure(1)
plt.plot(x, collisions, '--ro')
plt.xlabel('Scenarios')
plt.ylabel('Number of collisions detected')
plt.grid(axis='both')
plt.title('Graph showing the number of collisions detected\n using MAX algorithm for 1000 iterations')
plt.show()

# Detections
plt.figure(2)
plt.plot(x, detections, '--bo')
plt.xlabel('Scenarios')
plt.ylabel('Time taken to regenerate the MAX random number (s)')
plt.grid(axis='both')
plt.title('Graph showing the time taken to regenerate a MAX random number')
plt.show()
