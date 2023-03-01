# çapraz doğrulama (Cross Validation)
# modelleri ayarlarken görünmeyen veriler üzerinde genel model performansını artırmayı hedefliyoruz
# hiperparametre ayarı test setlerinde çok daha iyi performans sağlayabilir
# bununla birlikte parametrelerin test kümesine göre optimize edilmesi modelin görünmeyen veriler üzerinde daha kötü performans göstermesine
# neden olarak bilgi sıszıntısına neden olabilir.
# bunu düzeltmek için çapraz doğrulama yapabiliriz.

# K -katlama (K-Fold)
# modelde kullanılan eğitim verileri modeli doğrulamak için kullanılmak üzere
# k sayıda küçük kümeye bölünür. model daha sonra eğitim setinin k-1 katları üzerinde eğitilir.
# kalan kat daha sonra modeli değerlendirmek için bir doğrulama seti olarak kullanılır.

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)
k_folds = KFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=k_folds)
print("Cross Validition Scores:", scores)
print("Average CV Score:", scores.mean())
print("Number of CV scores usid in average:", len(scores))
