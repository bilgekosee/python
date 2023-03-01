# Bir renk haritasını farklı boyutlarda noktalarla birleştirebilirsiniz. Noktalar şeffafsa bu en iyi görselleştirilir:
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10*np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
