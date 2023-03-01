# Lojistik regresyon, sınıflandırma problemlerini çözmeyi amaçlar.
# Bunu, sürekli bir sonucu öngören doğrusal regresyonun aksine,
# kategorik sonuçları tahmin ederek yapar.


# En basit durumda, binom adı verilen iki sonuç vardır; buna bir örnek,
#  bir tümörün kötü huylu mu yoksa iyi huylu mu olduğunu tahmin etmektir.
#  Diğer durumların sınıflandırılması gereken ikiden fazla sonucu vardır,
# bu duruma multinomial denir. Çok terimli lojistik regresyon için yaygın
# bir örnek, 3 farklı tür arasında bir iris çiçeğinin sınıfını tahmin etmektir.

# Bağımsız değişkenleri X'te saklayın.
# Bağımlı değişkeni y'de saklayın
# 3,46 mm olduğu yerde tümörün kanserli olup olmadığını tahmin edin:

import numpy
from sklearn import linear_model
# tümörün cm cinsinden boyutu
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92,
                4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)

# tümörün iyi  kötü huylu olduğunu gösteren durum
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))

print(predicted)
