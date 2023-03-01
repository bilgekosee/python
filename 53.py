from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')


x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(
    n_clusters=2, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
