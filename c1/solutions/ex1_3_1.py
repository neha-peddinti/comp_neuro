from matplotlib import pyplot as plt
import numpy as np

'''
Ch 1, Ex. 3.1.
Generates spike train with the Poisson spike
generator from Ex. 1, and computes an autocorrelation
histogram.
'''

T = 10
#dt = .01
t = 0
r = 100

# get times for Poisson spikes
spikes = []
times = [] # autocorrelation, all possible intervals
while t < T:
    x = np.random.uniform(0.0, 1.0)
    i = -1*np.log(x)/r # current isi
    t += i
    if t < T:
        spikes.append(t)

# autocorrelation
for i in spikes:
    for j in spikes:
        times.append(j-i)

# plot autocorrelation histogram
plt.hist(times, bins=np.arange(-.5,.5,.01))
plt.title('autocorrelation histogram')
plt.xlabel('interval between any 2 spikes (s)')
plt.show()
