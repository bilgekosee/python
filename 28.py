# yeşil renge sahip 4 çubuk çizin
# çubukların genişliğini ayarlamak için width
# çubukların yüksekliğini ayarlmak için height
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

x = np.array(["ferrari", "mercedes", "audi", "bmw"])
y = np.array([100, 85, 60, 80])

plt.bar(x, y, color='green', width=0.6)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Yatay çubuklar için height kullanın width yerine
