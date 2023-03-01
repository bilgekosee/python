# HAT GENİŞLİĞİ
# Satırın genişliğini değiştirmek için anahtar kelime argümanını linewidthveya daha kısa olanı kullanabilirsiniz .lw
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')


ypoints = np.array([35, 62, 99, 10])

plt.plot(ypoints, lw='12.5', linestyle=':', c='r')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
