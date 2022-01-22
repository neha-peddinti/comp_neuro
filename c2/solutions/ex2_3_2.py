import numpy as np
import matplotlib.pyplot as plt

'''
Ch 2, Ex 3:

Takes STA generated in 'ex2_3_1.py' and 
renders plot from saved file.

Note: tau=0 occurs just before the spike,
while tau=12 occurs 12 time steps before
the spike.
'''

sta = np.load("ex2_3_sta.npy")

fig, ax = plt.subplots(4, 3, figsize=(10,7))

#clim = im.properties()['clim']

min = np.min(sta)
max = np.max(sta)
print(min)
print(max)

for i in range(4):
    for j in range(3):
        tau = i*3+j
        ax[i, j].set_title('tau = '+str(tau))
        ax[i, j].imshow(sta[:,:,tau], vmin=min, vmax=max)
        ax[i, j].set_xlabel('spatial x')
        ax[i, j].set_ylabel('spatial y')
        ax[i, j].set_xticks([], [])
        ax[i, j].set_yticks([], [])

im = ax[0, 0].imshow(sta[:,:,0], vmin=min, vmax=max)

cbar = fig.colorbar(im, format='%.0e')
cbar.ax.tick_params(labelsize=7)
for label in cbar.ax.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
plt.tight_layout()
plt.show()
