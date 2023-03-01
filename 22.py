# plt.plot()Her satır için bir işlev belirleyerek iki satır çizin :
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

y1 = np.array([3, 8, 9, 1, 2])
y2 = np.array([8, 2, 2, 34, 5])

plt.plot(y1)
plt.plot(y2)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Aynı fonksiyondaki her çizgi için x ve y ekseni noktalarını ekleyerek de birçok çizgi çizebilirsiniz plt.plot().
