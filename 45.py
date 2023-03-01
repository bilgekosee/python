# Peki ya R-kare puanı? R-kare puanı, veri kümemin modele ne kadar iyi uyduğunun iyi bir göstergesidir.
# Bu durumda, bir müşterinin mağazada kaldığı dakikalar ile ne kadar para harcadığı arasındaki ilişkiyi ölçmek istiyoruz.

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
#r2 = r2_score(train_y, mymodel(train_x))
# Şimdi aynı sonucu verip vermediğini görmek için modeli test verileriyle de test etmek istiyoruz.

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(test_y, mymodel(test_x))
# print(r2)

# Artık modelimizin uygun olduğunu belirlediğimize göre, yeni değerleri tahmin etmeye başlayabiliriz.
print(mymodel(5))
