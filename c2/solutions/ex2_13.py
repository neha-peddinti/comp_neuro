import numpy as np
import matplotlib.pyplot as plt

'''
Ch 2, Ex. 13.
Grating with preferred spatial frequency (k = k),
and preferred orientation (Theta = theta = 0).
Left eye views grating with spatial phase (Phi=Phi_L).
Right eye views grating with spatial phase (Phi=Phi_R).
Simple neurons with preferred spatial phase (phi=0).

Linear response of simple cells:
L1 = A/2*(cos(Phi_L)+cos(Phi_R))
L2 = A/2*(sin(Phi_L)+sin(Phi_L))

Complex cell response: L1^2+L2^2
L1^2 + L2^2 = (A^2/2)*(cos(Phi_L)cos(Phi_R)+sin(Phi_L)sin(Phi_R))
 = (A^2/2) * cos(Phi_L - Phi_R)

which is tuned to the dispairty between spatial phases (Phi_L-Phi_R).
Implicated in depth detection in the visual cortex.

Plot response (L = L1^2+L2^2) as a function of disparity d.
'''

A = 1

d = np.arange(-1*np.pi/2, np.pi/2, .1)
L = np.cos(d)*A**2/2

plt.xlabel('disparity (Phi_L - Phi_R) in radians')
plt.ylabel('complex neuron response L')
plt.plot(d, np.cos(d))
plt.show()
