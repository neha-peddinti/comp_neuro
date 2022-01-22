import numpy as np
import matplotlib.pyplot as plt

'''
Ch 2, Ex. 1.
Predicts the response of a neuron of the
electrosensory lateral-line lobe to an
approximate Gaussian white noise stimulus.

Computes firing rate, and the firing rate-stimulus
correlation function.
'''

r0 = 50 # Hz

# linear kernel function
def D(tau):
   return -1*np.cos(2*np.pi*(tau-.020)/.140)*np.exp(-1*tau/.060) # Hz/s
d = lambda tau: D(tau)
   
# approximate Gaussian white noise stimulus
dt = .010 # ms
a = 1 # from Q_{ss}(tau) = a*dirac(tau)
T = 10 # total stimulus duration
t = np.arange(0.0, T, dt)
stim = np.random.normal(loc=0, scale=(a/dt), size=(int(T/dt),))
kernel = d(t)

# firing rate estimate
# r = r0 + np.convolve(kernel, stim, mode='same')
def rate(t):
    sum = 0
    for tau in np.arange(0, t, dt):
        sum += D(tau)*stim[int((t-tau)/dt)]
    return r0 + sum
r = np.vectorize(rate)
firing_rate = r(t)

# plot d(t) in reverse, stim(t), and r(t)
fig, axs = plt.subplots(5)
axs[0].plot(t, kernel)
axs[0].set_xlim(0, 1)
axs[0].invert_xaxis()
axs[0].set_title('Linear kernel estimate D(tau) vs. tau')
axs[1].plot(t, stim)
axs[1].set_title('Gaussian white noise stimulus vs. t (s)')
axs[2].plot(t, firing_rate)
axs[2].set_title('Linear firing rate estimate (Hz) vs t (s)')

# firing rate-stimulus correlation function
def q_rs(tau):
    sum = 0
    for t in np.arange(0, T, dt):
        sum += firing_rate[int(t/dt)]*stim[int((t+tau)/dt)%int(T/dt)]
    return sum / T
corr_tau = np.arange(-1, 1, dt)
Q_rs = np.vectorize(q_rs)
Q_rs_vals = Q_rs(corr_tau)
axs[3].plot(corr_tau, Q_rs_vals)
axs[3].set_title('Firing rate-stimulus correlation function Q_rs(tau)')

# optimal kernel (compared to D)
D_optimal = Q_rs_vals[::-1]/a 

axs[4].plot(corr_tau, D_optimal)
axs[4].set_xlim(-.5,.5)
axs[4].invert_xaxis()
axs[4].set_title('Optimal kernel D(tau) v. tau')

for ax in axs:
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax.locator_params(axis='y', nbins=4)
    for label in ax.yaxis.get_ticklabels()[::2]:
        label.set_visible(False)
        label.set_fontsize(5)

fig.tight_layout()
plt.show()
