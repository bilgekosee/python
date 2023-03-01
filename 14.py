# Matplotlib, bir görselleştirme yardımcı programı olarak hizmet veren, python'da düşük seviyeli bir grafik çizim kitaplığıdır.
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


xpoints = np.array([1, 9])
ypoints = np.array([3, 11])

plt.plot(xpoints, ypoints)
plt.show()
