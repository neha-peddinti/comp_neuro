import numpy as np
from math import *
import matplotlib.pyplot as plt

"""
Ch 3, Ex. 1.
Neuron responds to 2 stimuli ("plus" or "minus").
    p[r|+]: response to + stim, mean "rp"
    p[r|-]: response to - stim, mean "rm"
    Both distributions are Gaussian with variace "sd"^2

1) Plot ROC curves for different d' values.

1) Simulate the two-alternative forced choice task.
    Randomly pick stimulus order (+/- or -/+).
    Use the order to sample for r1 (+/-) and r2 (-/+) from p[r|+-].
    Correct prediction if r1 > r2 for stim (+/-) or r1 < r2 for stim (-/+).

2) Find areas under corresponding ROC curves.

3) Compare values (they should be equal).
"""

# Plot ROC curves for different d values.
# P[correct] = p
p = .5*erfc(-1*d/2)

# finish this at some point
