# Kesinlik
# Doğruluk, modelin ne sıklıkla doğru olduğunu ölçer.
# (Gerçek Pozitif + Gerçek Negatif) / Toplam Tahmin

import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

Accuracy = metrics.accuracy_score(actual, predicted)

print(Accuracy)
