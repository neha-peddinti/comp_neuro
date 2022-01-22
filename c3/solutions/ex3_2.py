import numpy as np
import matplotlib.pyplot as plt
from math import *

"""
Ch 3, Ex. 2.
Random-dot discrimination experiment
1) Randomly choose plus or minus stimulus.
2) Generate neural response.
    Sample from p[r|+] if plus stim; otherwise p[r|-].
3) Generate threshold.
4) Determine the fraction of correct predictions (1000 trials) for different d values from 0 to 10.
5) Plot percent correct vs d.
6) Find a(z) and b(z) for 0 <= z <= 140, for different d values.
7) Plot ROC curves.

"""
# d: discriminability
# t: trial number
# rm: <r>- = average firing rate for - stimulus
# rp: <r>+ = average firing rate for + stimulus
# sd: standard deviation of both p[r|+] and p[r|-] distributions
# z: threshold (halfway between rm and rp)
# n: number of trials

rm = 20 # Hz
sd = 10 # Hz
n = 1000

def response(stim, rm, rp):
    if stim == 0:
        return np.random.normal(rm, sd)
    return np.random.normal(rp, sd)

def a(z, rm, sd):
    return .5*erfc((z-rm)/(sqrt(2)*sd))

def b(z, rp, sd):
    return .5*erfc((z-rp)/(sqrt(2)*sd))

a_vectorized = np.vectorize(a)
b_vectorized = np.vectorize(b)

d = np.arange(0, 11)
correct = np.zeros(len(d))

for i in range(len(d)):
    # find % correct predictions after n trials
    rp = rm + sd*d[i]
    z = rm + (sd/2)*d[i]
    for t in range(n):
        stim = np.random.randint(2)   # 0 (-) or 1 (+)            
        r = response(stim, rm, rp)
        if (r >= z and stim == 1) or (r < z and stim == 0):
            correct[i] += 1
    # plot ROC curve for this value of d = d[i]
    z = np.arange(140)
    a_values = a_vectorized(z, rm, sd)
    b_values = b_vectorized(z, rp, sd)
    plt.plot(a_values, b_values)
    plt.text(a_values[-n/10], b_values[-n/10], "d={}".format(d[i]))
plt.xlabel('a')
plt.ylabel('b')
plt.title('ROC curves')
plt.show()
        
correct /= 10

plt.plot(d, correct)
plt.xlabel('discriminability d (Hz)')
plt.ylabel('percent correct')
plt.title('random-dot discrimination experiment simulation results')
plt.show()

