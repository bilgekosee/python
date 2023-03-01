# birini dışarıda bıralk(LOO)
# k katlı leaveoneout gibi eğitim veri setindeki bölme sayısını seçmek yerine doğrulamak için 1 gözlem ve eğitmek içinn-1 gözlem kullanın. bu yöntem kapsamlı bir tekniktir.
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

loo = LeaveOneOut()

scores = cross_val_score(clf, X, y, cv=loo)

print("cross validation scores:", scores)
print("average cv scores: ", scores.mean())
print("number of cv scores used in average:", len(scores))

# Gerçekleştirilen çapraz doğrulama puanlarının sayısının veri kümesindeki gözlem sayısına eşit olduğunu gözlemleyebiliriz. Bu durumda iris veri setinde 150 gözlem vardır.
