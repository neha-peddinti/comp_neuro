import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

'''
Ch 1, Ex. 2.
Poisson spike generator with refractory period
that allows the neuron to recover after each spike
and allows for a time-dependent firing rate.
Firing rate starts at r_max Hz, drops to 0 after a
spike, and recovers exponentially back to r_max
with time constant tau.

Generates histogram of interspike intervals.
Computes coefficinet of variation for the ISIs,
and the Fano factor for spike counts.
'''

T = 50
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

# cv
isi_std = np.std(isi)
isi_mean = np.mean(isi)
cv = isi_std/isi_mean
print('cv: ', cv)

# fano factor for spike counts obtained over 100ms intervals
spike_counts = []
for i in range(1000):
    t = .100 # (s)
    # get random counts within an interval of length t
    x = np.random.randint(0, len(isi)) # starting index
    count = 0
    val0 = isi[np.random.randint(0, len(isi))]
    val = 0
    while (val < val0 + t) and (x < len(isi)):
        val += isi[x]
        x += 1
        count += 1
    spike_counts.append(count)

print('fano factor: ', (np.var(spike_counts)/np.mean(spike_counts)))

# plot isi histogram
plt.hist(isi, bins=np.arange(0,.1,.001))
plt.title('interspike interval dist.')
plt.xlabel('interspike interval (s)')
plt.show()
