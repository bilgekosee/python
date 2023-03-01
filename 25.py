import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
# Argüman ile noktaların boyutunu değiştirebilirsiniz s ve alpha ile şeffaflığı ayarlayabilirsiniz
plt.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha=0.5)

plt.colorbar()

plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# birçok mevcut renk haritası var viridis bunlardan sadece biri
