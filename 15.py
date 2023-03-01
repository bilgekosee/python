# Three lines to make our compiler able to draw:
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
