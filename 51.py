# F puanı
# F-skoru, kesinlik ve duyarlılığın "harmonik ortalamasıdır".
# Hem yanlış pozitif hem de yanlış negatif vakaları dikkate alır ve dengesiz veri kümeleri için iyidir.

import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

F1_score = metrics.f1_score(actual, predicted)
print(F1_score)
