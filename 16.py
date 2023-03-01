import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


xpoints = np.array([12, 8, 89, 1])
ypoints = np.array([33, 42, 34, 75])

plt.plot(xpoints, ypoints)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
