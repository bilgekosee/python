# marker Her noktayı belirli bir işaretleyici ile vurgulamak için anahtar kelime bağımsız değişkenini kullanabilirsiniz
# eğer yıldızla işaretlemek iatiyorsak o yerine *  yazarız
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

ypoints = np.array([23, 32, 86])
plt.plot(ypoints, marker='o')
plt.show()

plt.savefig(sys.studout.buffer)
sys.stdoutt.flush()
