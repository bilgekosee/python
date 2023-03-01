# normal gauss çan eğrisi veri dağılımı
import matplotlib.pyplot as plt
import numpy
import matplotlib
import sys
matplotlib.use('TkAgg')

# Ortalama değerin 5,0 ve standart sapmanın 1,0 olduğunu belirtiyoruz.
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)  # 100 çubuklu hist. çizmemizi sağlıyo
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
