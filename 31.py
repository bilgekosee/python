# 0 ile 5 arasında 250 rasgele kayan nokta içeren bir dizi oluşturun ve histogram grafik çizin:

import matplotlib.pyplot as plt
import sys
import numpy
import matplotlib
matplotlib.use('TkAgg')
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
