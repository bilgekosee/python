# Pandas modülü, csv dosyalarını okumamızı ve bir DataFrame nesnesi döndürmemizi sağlar.
# Sklearn modülünden, LinearRegression()yöntemi doğrusal bir regresyon nesnesi oluşturmak için kullanacağız.
import pandas
from sklearn import linear_model
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)


# predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
