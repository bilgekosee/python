# Eğitim setini kullanarak modeli eğitirsiniz .
# Test setini kullanarak modeli test edersiniz
# veri setimiz bir mağazadaki 100 müşteriyi ve onların alışveriş alışkanlıklarını göstermektedir.
# Veri seti neye benziyor? Bence en uygunu bir polinom regresyon olacaktır , bu yüzden bir polinom regresyon çizgisi çizelim.

import matplotlib.pyplot as plt
import numpy
import sys
import matplotlib
matplotlib.use('TkAgg')

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)


plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# X ekseni, bir satın alma işlemi gerçekleştirmeden önceki dakika sayısını temsil eder.
# Y ekseni, satın alma için harcanan para miktarını temsil eder.

# Eğitime/Test'e Ayrılma
# Eğitim seti, orijinal verilerin %80'inin rastgele bir seçimi olmalıdır .
# Test seti kalan %20 olmalıdır.
