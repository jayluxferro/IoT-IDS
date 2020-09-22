import func
import db
import matplotlib.pyplot as plt
import numpy as np

n1 = [[], []]
n2 = [[], []]
n3 = [[], []]

for data in db.getTable("battery"):
    if data['node'] == 1:
        n1[data['scenario']].append(data['power'])
    elif data['node'] == 2:
        n2[data['scenario']].append(data['power'])
    else:
        n3[data['scenario']].append(data['power'])


x = np.linspace(1, len(n1[0]), len(n1[0]))

dataPoints = [n1, n2, n3]
nodes = ['N1', 'N2', 'N3']
counter = 0
for n in dataPoints:
    plt.figure()
    plt.plot(x, n[0], '-o', x, n[1], '-o')
    plt.legend(['{} - Normal'.format(nodes[counter]), '{} - Active'.format(nodes[counter])])
    plt.xlabel('Minutes')
    plt.ylabel('Power (W)')
    plt.show()
    counter += 1
    print(np.mean(n[0]), np.mean(n[1]))
    print('')
