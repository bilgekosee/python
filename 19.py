# İşaretçilerin boyutunu ayarlamak için anahtar sözcük bağımsız değişkenini markersizeveya daha kısa sürümünü kullanabilirsiniz :ms
# işaretçilerin kenar rengini markeredgecolor ile belirleyebiliyoruz kısaltılmışı mec
# işaretçilerin kenarının içindeki rengide belirleyebiliyoruz markerfacecolor ile kısaltılmışı mfc
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

ypoints = np.array([12, 18, 21, 49])

plt.plot(ypoints, marker='p', ms=20, mec='k', mfc='#4a4e69')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
