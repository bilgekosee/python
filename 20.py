# Çizilen çizginin stilini değiştirmek için argüman linestyleveya daha kısa anahtar kelimesini kullanabilirsiniz :ls
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

ypoints = np.array([25, 36, 48, 98])
plt.plot(ypoints, linestyle='dotted', c='c')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# kısaltmaları linestyle olarak yazılabilir ls, dottedolarak yazılabilir : , dashedolarak yazılabilir --.
# Satırın rengini ayarlamak için anahtar kelime bağımsız değişkenini color veya daha kısa olanı kullanabilirsiniz :c
