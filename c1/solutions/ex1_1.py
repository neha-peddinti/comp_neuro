from matplotlib import pyplot as plt
import numpy as np

'''
Ch 1, Ex. 1.
Poisson spike generator that generates neuron
spikes for T seconds with a constant rate of 
r Hz, and records the times of spike occurrences.

Generates histogram of interspike intervals.
Mathematically, this should look like an 
exponential distribution.
'''

T = 50
#dt = .01
t = 0
r = 100

# get times for Poisson spikes
spikes = []
isi = []
while t < T:
    x = np.random.uniform(0.0, 1.0)
    i = -1*np.log(x)/r # current isi
    t += i
    if t < T:
        spikes.append(t)
    isi.append(i)

# coefficient of variation (should be around 1)
isi_std = np.std(isi)
isi_mean = np.mean(isi)
cv = isi_std/isi_mean
print('cv: ', cv)

# fano factor for spike counts obtained over count intervals of length t
spike_counts = []
for i in range(1000):
    t = .0200 # count interval of 20ms
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
