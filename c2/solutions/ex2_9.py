from numpy import *
from math import *
import matplotlib.pyplot as plt
import scipy.integrate as integrate

'''
Ch 2, Ex. 9.
Plot the temporal response of a simple cell in response
to an oscillating stimulus (a temporal grating).
Plot the temporal response of a complex cell in response
to the same stimulus.

The complex cell has double the frequency of the simple
cell, and has a continuous response.
'''

# function to integrate (kernel*stim)
a = 1/.015  # in (s^-1)
print(a)
omega = 6*pi
def f(tau, t):
    return a*exp(-1*a*tau)*((a*tau)**5/factorial(5)-(a*tau)**7/factorial(7))*cos(omega*(t-tau))

# linear response L from integrating previous function
L = []
L2 = []
time = arange(0, 1, .005)
for t in time:
    I = integrate.quad(f, 0, inf, args=(t))
    L.append(max(I[0],0))
    L2.append(I[0]**2)

# simple cell response L oscillates with same omega as stimulus
# must be rectified due to negative components
plt.title('simple cell')
plt.xlabel('t (s)')
plt.ylabel ('temporal response L(t)')
plt.plot(time, L)
plt.show()

# complex cell response oscillates with double the frequency
# no negative components; continuous response
plt.title('complex cell')
plt.xlabel('t (s)')
plt.ylabel('temporal response L2(t)')
plt.plot(time, L2)
plt.show()
