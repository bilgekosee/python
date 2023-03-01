# IZGARA ARAMASI: iki veya daha fazla parametre için değer seçmek zorunda kaldıysak değer kümelerinin tüm kombinasyonlarını
# değerlendirerek bir değer ızgarası oluşturma tekniği.

from sklearn import datasets
# iris çiçeklerini sınıflandırmak için lojistik model
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()

X = iris['data']
y = iris['target']

# Modelin oluşturulması, modelin bir sonuç bulmasını sağlamak için max_iter değerini daha yüksek bir değere ayarla
logit = LogisticRegression(max_iter=10000)

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []

for choice in C:
    logit.set_params(C=choice)
    logit.fit(X, y)
    scores.append(logit.score(X, y))

print(scores)


# Lojistik regresyon modelimizi, onu eğitmek için kullanılan verilerin
# aynısını kullanarak puanladık. Model bu verilere çok yakınsa,
# görünmeyen verileri tahmin etmede harika olmayabilir. Bu istatistiksel
# hata, aşırı uydurma olarak bilinir
