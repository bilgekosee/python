# çubuklar ile grafik çizme
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

x = np.array(["A", "B", "C", "D"])
y = np.array([2, 6, 8, 10])

plt.bar(x, y, color="red")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Çubukların dikey yerine yatay olarak görüntülenmesini istiyorsanız, bar() yerine barh()işlevi kullanın:
