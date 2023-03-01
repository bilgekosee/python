# tabakalı k-katlama (Stratified K-Fold)
# sınıfların dengesiz olduğu durumlarda hem tren hem de doğrulama kümelerindeki
# dengesizliği hesaba katmak için bir yola ihtiyacımız var. Bunu yapmak için hedef sınıfları katmanlara ayırabiliriz.bu da her iki kümenin
# tüm sınıflarının eşit orana sahip olacağı anlamına gelir.

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

sk_folds = StratifiedKFold(n_splits=5)

scores = cross_val_score(clf, X, y, cv=sk_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
