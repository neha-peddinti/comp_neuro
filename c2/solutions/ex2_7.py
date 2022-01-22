from numpy import *
import matplotlib.pyplot as plt

'''
Ch 2, Ex. 7.
Compute the spatial part of the linear response
of a simple cell with a separable space-time
receptive field (RF) to a sinusoidal grating.

Stimulus function s:
s = A*cos(K*x*cos(Theta)+K*y*sin(Theta)-Phi)
Theta = orientation of grating
Phi = phase
x, y = spatial location in RF

Gabor function as spatial RF kernel D:
D = 1/(2*pi(sig**2)*exp(-1*x**2/(2*sig**2)-y**2/(2*sig**2))*cos(k*x-phi)

Determine the neuron's preferred spatial frequency K
and its preferred spatial phase Phi.
'''

# sinusoidal grating stimulus function
A = 50
Theta = 0

# Gabor function as spatial RF kernel
sig = 1 # in degrees
phi = 0
k = 2   # preferred spatial frequency of the grating

# plot linear neuron response Ls vs stim spatial freq K
# assume stim spatial phase = preferred spatial phase = 0
K = arange(0, 20)
L = A*exp(-1*sig**2*(k**2+K**2)/2)*cosh(sig**2*k*K*cos(Theta))
print('preferred spatial frequency K: ',K[argmax(L)])

plt.xlabel('spatial frequency K of stim')
plt.ylabel('linear response L of neuron')
plt.plot(K, L)
plt.show()

# assume preferred orientation = stim orien. = 0
# find preferred spatial phase
K = 2
Phi = arange(-3, 3, .1)
L = A/2*exp(-1*sig^2*(k-K)^2/2)*cos(phi-Phi)
print('preferred spatial phase Phi: ', Phi[argmax(L)])

plt.xlabel('spatial phase Phi of stim')
plt.ylabel('linear response L of neuron')
plt.plot(Phi, L)
plt.show()

# Results are preferred K = 2 and preferred Phi = 0.
# This aligns with the k and phi inputs into the RF.
