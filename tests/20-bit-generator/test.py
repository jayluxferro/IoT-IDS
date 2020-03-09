import time
import matplotlib.pyplot as plt
import numpy as np
times = []

for x in range(50):
    start = time.time()
    for i in range(1, 2**20):
        print(i)

    stop = time.time()
    times.append(stop - start)

print(times)
plt.figure()
plt.plot(np.linspace(1, len(times), len(times)), times, '-ro')
plt.xlabel('Number of attempts')
plt.ylabel('Time (s)')
plt.title('Analysis of MAX Algorithm')
plt.show()
