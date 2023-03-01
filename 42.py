# Verileri ölçeklendirmek için farklı yöntemler vardır, bu eğitimde standardizasyon adı verilen bir yöntem kullanacağız.
# Standardizasyon yöntemi şu formülü kullanır:
#z = (x - u) / s
# Nerede z yeni değer, x orijinal değer, u ortalama ve s standart sapmadır.

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
