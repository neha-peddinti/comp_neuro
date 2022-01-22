import numpy as np
import matplotlib.pyplot as plt

'''
Ch 1, Ex. 6.
Approximate white-noise stimulus.
Plots stimulus, its autocorrelation function,
and its power spectrum.

Autocorrelation has a few spikes at values
besides t=0 because the limit on quantity of
generated data leads to imperfections.
Spikes in the power spectrum (which should be
constant, and still seems relatively stable)
are related to this as well.
'''

# Approx WN stimulus values from PD with mean=0, variance=a/dt
dt = .01 # (s)
a = 1 # from Q_{ss}(tau) = a*dirac(tau)
T = 10 # (s), total stimulus duration

fig, axs = plt.subplots(3, figsize=(15,10))

# plot WN stimulus
s = np.random.normal(loc=0, scale=(a/dt), size=(int(T/dt),))
t = np.arange(0.0, T, dt)

axs[0].plot(t, s)
axs[0].set_title('stimulus s(t) value')
axs[0].set_xlabel('time (s)')

# plot autocorrelation histogram
axs[1].acorr(s)
axs[1].set_title('autocorrelation of s(t)')
axs[1].set_xlabel('lag (s)')

# plot power spectrum of s(t)
fourier_transform = np.fft.rfft(s)
power_spectrum = np.square(np.abs(fourier_transform))
frequency = np.linspace(0, .3/2, len(power_spectrum))

axs[2].plot(frequency, power_spectrum)
axs[2].set_title('power spectrum')
axs[2].set_xlabel('frequency')

fig.tight_layout()
plt.show()
