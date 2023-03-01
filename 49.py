# Hassasiyet (Geri Çağırma)
# Tüm pozitif vakaların yüzde kaçının pozitif olduğu tahmin ediliyor?
# Duyarlılık (bazen Hatırlama olarak adlandırılır), modelin pozitifleri tahmin etmede ne kadar iyi olduğunu ölçer.

import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

Sensitivity_recall = metrics.recall_score(actual, predicted)
print(Sensitivity_recall)
