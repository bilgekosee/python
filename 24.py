# İşlevle, subplot()tek bir şekilde birden fazla grafik çizebilirsiniz:
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')


x = np.array([0, 3, 2, 5])
y = np.array([5, 63, 2, 3])
plt.subplot(1, 2, 1)  # 1 satır, 2 sütuna sahiptir ve bu çizim ilk çizimdir
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 30, 50, 40])
plt.subplot(1, 2, 2)
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
