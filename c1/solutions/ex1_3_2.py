from matplotlib import pyplot as plt
import numpy as np

'''
Ch 1, Ex. 3.1.
Generates spike train with the Poisson spike
generator from Ex. 2, and computes an autocorrelation
histogram.
'''

T = 10
#dt = .01
t = 0
r_max = 100

# get initial times for Poisson spikes
isi = []
while t < T:
    x = np.random.uniform(0.0, 1.0)
    i = -1*np.log(x)/r_max # current isi
    t += i
    
    if t < T:
        isi.append(i)

# spike thinning, with time constant tau (s) for recovery
new_isi = []
spikes = []
t = 0
tau = .010 # .001 to .020 (s)

for i in range(len(isi)):
    # get firing rate at the time of each spike (t=isi)
    t += isi[i]
    r = r_max*(1-np.exp(-1*t/tau))

    # prob. of keeping spike = r(t)/r_max
    if np.random.uniform(0.0, 1.0) < r/r_max:
        new_isi.append(t)
        t = 0

isi = new_isi
t = 0
for i in isi:
    t += i
    spikes.append(t)

# autocorrelation
times = []
for i in spikes:
    for j in spikes:
        times.append(j-i)

# plot autocorrelation histogram
plt.hist(times, bins=np.arange(-.505,.505,.005))
plt.title('autocorrelation histogram')
plt.xlabel('interval between any 2 spikes (s)')
plt.show()
