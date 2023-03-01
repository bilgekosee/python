# Her ikisi de normal bir veri dağılımından 1000 rasgele sayı ile doldurulmuş iki dizi oluşturalım.

# İlk dizi, 1.0'lık bir standart sapma ile 5.0'a ayarlanmış ortalamaya sahip olacaktır.

# İkinci dizi, 2,0 standart sapma ile ortalama olarak 10,0 olarak ayarlanacaktır:

import matplotlib.pyplot as plt
import numpy
import matplotlib
import sys
matplotlib.use('TkAgg')


x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
