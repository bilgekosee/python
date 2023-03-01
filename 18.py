# İşaretçiyi belirtmek için kısayol dize notasyonu parametresini de kullanabilirsiniz
# şu söz dizimi ile yazılır:marker|line|color
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')


ypoints = np.array([52, 77, 41])

plt.plot(ypoints, '*:r')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
