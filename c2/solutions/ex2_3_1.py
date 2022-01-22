import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt

'''
Ch 2, Ex 3.
Uses neuron response data of a cat LGN cell
to 2D visual images (Kara, P, Reinagel, P, 
& Reid, RC, 2000) to calculate the spike-
triggered average image for each of the 12
time steps before each spike, and display
them all (equivalent of MATLAB imagesc).

Result is a central visual receptive field (RF)
that changes sign over time, indicating that
the cell responds to stimuli in which the
contrast starts a neutral (zero) value, drops
to a dark value in the center of the RF, and
rapidly reverses to a bright value.

Stores STA in file 'ex2_3_sta.npy'.
'''

# import c2p3.mat data as arrays
mat = spio.loadmat('../data/c2p3.mat', squeeze_me=True)
counts = mat['counts']
stim = mat['stim']

# counts: number of spikes in each 15.6 ms bin
dt = 15.6 # ms

# stim: 32767 images, each 16x16
#   stim(x,y,t) is the image value at (x,y) presented at time-step t
dim = 16

# find STA of the images for each of the 12 time steps before each spike
# weight each stim by the number of spikes in the bin
max_step = 12
sta = np.zeros((dim,dim,max_step))
# separate STA for each time step until max_step is reached
#for i in range(max_step):
for i in range(max_step):
    # for each value in counts, weight the stim i before the counts index
    count = 0
    for t in range(i, len(counts)):
        for x in range(dim):
            for y in range(dim):
                sta[x, y, i] += counts[t]*stim[x, y, t-i]
        count += counts[t]
    # divide each pos by total spike count for average stim value
    for pos in [(x,y) for x in range(dim) for y in range(dim)]:
        sta[x, y, i] /= float(count)

# save sta to file
np.save("ex2_3_sta.npy", sta)

# sum images across x dimension to produce figure like fig 2.25C
