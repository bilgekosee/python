# Birini Dışarıda Bırak fikrinin basit bir nüanslı farkıdır, çünkü doğrulama setimizde kullanacağımız p sayısını seçebiliyoruz.
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeavePOut, cross_val_score
X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

lpo = LeavePOut(p=2)

scores = cross_val_score(clf, X, y, cv=lpo)

print("cross validation scores: ", scores)
print("average cv score :", scores.mean())
print("number of cv scores used in average: ", len(scores))

# Gördüğümüz gibi, bu kapsamlı bir yöntem, ap = 2 olsa bile, Birini Dışarıda Bırak'a göre çok daha fazla puan hesaplıyoruz, ancak kabaca aynı ortalama CV puanını elde ediyor.
