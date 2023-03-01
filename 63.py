'''Bootstrap Aggregation (torbalama), sınıflandırma veya regresyon 
sorunları için fazla uydurmayı çözmeye çalışan bir birleştirme yöntemidir.
Torbalama, makine öğrenimi algoritmalarının doğruluğunu ve performansını
iyileştirmeyi amaçlar. Bunu, orijinal bir veri kümesinin rasgele alt 
kümelerini değiştirerek yapar ve her bir alt kümeye bir sınıflandırıcı 
(sınıflandırma için) veya regresör (gerileme için) yerleştirir. Her bir
alt küme için tahminler daha sonra, sınıflandırma için çoğunluk oyu 
veya regresyon için ortalama alma yoluyla toplanır ve tahmin doğruluğu artar.'''

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

data = datasets.load_wine()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=22)

dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)

print("train data accuarcy:", accuracy_score(
    y_true=y_train, y_pred=dtree.predict(X_train)))

print("Test data accuracy:", accuracy_score(y_true=y_test, y_pred=y_pred))
