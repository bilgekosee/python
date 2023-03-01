from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Verileri bir dizi noktaya dönüştürün
data = list(zip(x, y))

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
