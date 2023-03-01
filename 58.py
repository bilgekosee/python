# verilerimiz dizelerle temsil edilen kategorilere sahip olduğunda bunları
# genellikle  yalnızca sayısal verileri kabul eden makine örenimi modelleri
# eğitmek için kullanmak zor olacaktır.
# kategorik verileri yok saymak ve bilgileri modelimizin dışında bırakmak yerine
# verileri modellerinizde kullanabilecek şekilde dönüştürebilirsiniz.


'''import pandas as pd

cars = pd.read_csv('data.csv')

print(cars.to_string())'''

# Araba veya Model sütununu sayısal olmadığı için verilerimizde
# kullanamıyoruz. Kategorik bir değişken olan Araba veya Model ile sayısal
#  bir değişken olan CO2 arasında doğrusal bir ilişki belirlenemez.


# Bu sorunu çözmek için, kategorik değişkenin sayısal bir temsiline sahip
# olmamız gerekir. Bunu yapmanın bir yolu, kategorideki her grubu temsil eden bir sütuna sahip olmaktır.

import pandas as pd
cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())
