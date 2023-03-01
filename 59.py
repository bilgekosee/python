import pandas as pd
from sklearn.linear_model import LinearRegression

cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])

X = pd.concat([cars[['Volume', 'Weight']],
               ohe_cars], axis=1)
y = cars['CO2']

regr = LinearRegression()
regr.fit(X, cars['CO2'])
predictedCO2 = regr.predict(
    [[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

print(predictedCO2)
