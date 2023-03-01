# Katsayı, bilinmeyen bir değişkenle ilişkiyi açıklayan bir faktördür.
import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# Sonuç dizisi, ağırlık ve hacmin katsayı değerlerini temsil eder.
# Ağırlık: 0,00755095
# Hacim: 0,00780526

# Bu değerler bize ağırlık 1kg artarsa ​​CO2 emisyonunun 0,00755095g arttığını söylüyor.
