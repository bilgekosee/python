import pandas
df = pandas.read_csv("data2.csv")
# print(df)
# Bir karar ağacı oluşturmak için tüm verilerin sayısal olması gerekir.
# Pandas, map()değerlerin nasıl dönüştürüleceğine ilişkin bilgileri içeren bir sözlük alan bir yönteme sahiptir.
#{'UK': 0, 'USA': 1, 'N': 2}

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
# print(df)
# Özellik sütunları, tahmin etmeye çalıştığımız sütunlardır ve hedef sütun, tahmin etmeye çalıştığımız değerlerin bulunduğu sütundur.
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)
