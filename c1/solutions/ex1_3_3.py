from matplotlib import pyplot as plt
import numpy as np

'''
Ch 1, Ex. 3.3.
Generates spike train with a Poisson spike
generator that has an oscillating time-dependent
firing rate, and computes an autocorrelation
histogram.

Note: The frequency of the oscillating firing
rate is f=40 Hz for T=.025s, which is a gamma
wave in the brain and is of particular interest
in Alzheimer's research.
'''

T = 20 # trial duration (s)

# get initial times for Poisson spikes
spikes = []
t = 0
r_max = 200

while t < T:
    x = np.random.uniform(0.0, 1.0)
    i = -1*np.log(x)/r_max # current isi
    t += i
    
    if t < T:
        spikes.append(t)

# spike thinning
new_spikes = []
for i in spikes:
    # time-dependent firing rate function r(t); (T=25 ms, A=100Hz)
    r = 100*(1+ np.cos(2*np.pi*i/.025))

    # prob. of keeping spike = r(t)/r_max
    if np.random.uniform(0.0, 1.0) < r/r_max:
        new_spikes.append(i)

spikes = new_spikes

# autocorrelation
times = []
for i in spikes:
    for j in spikes:
        times.append(j-i)

# plot autocorrelation histogram
fig, axs = plt.subplots(2)

axs[0].hist(times, bins=np.arange(-.1,.1,.005))
axs[0].set_title('autocorrelation histogram')
axs[0].set_xlabel('interval between any 2 spikes (s)')

axs[1].hist(spikes, bins=np.arange(0, 5, .025))
axs[1].set_title('spike train')
axs[1].set_xlabel('t (s)')
fig.tight_layout()
plt.show()
