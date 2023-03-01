from sklearn.tree import plot_tree
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')

data = datasets.load_wine()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=22)
oob_model = BaggingClassifier(n_estimators=12, oob_score=True, random_state=22)

oob_model.fit(X_train, y_train)

clf = BaggingClassifier(n_estimators=12, oob_score=True, random_state=22)
clf.fit(X_train, y_train)

plt.figure(figsize=(30, 20))
plot_tree(clf.estimators_[0])
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
