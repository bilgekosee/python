# Matplotlib'de, hist()histogramlar oluşturmak için işlevi kullanırız.
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

x = np.random.normal(212, 253, 63)

plt.hist(x)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
