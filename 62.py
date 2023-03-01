# K-MEANS

# K-means, veri noktalarını kümelemek için denetimsiz bir öğrenme yöntemidir.
# Algoritma, her kümedeki varyansı en aza indirerek veri noktalarını yinelemeli olarak K kümeye böler.


# İLK OLARAK HER BİR VERİ NOKTASI RASTGELKE OLARAK k kümesinden birine atanır.
# ardından her bir kümenin ağırlık merkezini hesaplıyoruz ve her veri noktasnı en yakın merkez
# noktasına sahip kümeye yeniden atıyoruz. her veri noktası için küme atamaları artık değişmeyene kadar bu işlemi tekrarlıyoruz.

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys
import matplotlib
matplotlib.use('TkAgg')

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
inertias = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title("elbow method")
plt.xlabel("number of clusters")
plt.ylabel("inertia")
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Dirsek yöntemi, 2'nin K için iyi bir değer olduğunu gösterir, bu nedenle sonucu yeniden eğitir ve görselleştiririz
