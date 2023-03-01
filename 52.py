# Hiyerarşik kümeleme
"""Hiyerarşik kümeleme, veri noktalarını kümelemek için denetimsiz 
bir öğrenme yöntemidir. Algoritma, veriler arasındaki farklılıkları 
ölçerek kümeler oluşturur. Denetimsiz öğrenme, bir modelin eğitilmesi 
gerekmediği ve bir "hedef" değişkene ihtiyacımız olmadığı anlamına gelir.
 Bu yöntem, bireysel veri noktaları arasındaki ilişkiyi görselleştirmek 
 ve yorumlamak için herhangi bir veri üzerinde kullanılabilir."""

"""Aşağıdan yukarıya yaklaşımı izleyen bir tür hiyerarşik kümeleme 
 olan Aglomerative Clustering'i kullanacağız. Her veri noktasını kendi 
 kümesi olarak ele alarak başlıyoruz. Ardından, daha büyük kümeler 
 oluşturmak için aralarındaki en kısa mesafeye sahip kümeleri 
 birleştiririz. Bu adım, tüm veri noktalarını içeren büyük bir küme oluşana kadar tekrarlanır."""

from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib
import numpy as np
import sys
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Şimdi koğuş bağlantısını öklid mesafesini kullanarak hesaplıyoruz ve bir dendrogram kullanarak görselleştiriyoruz:
data = list(zip(x, y))
linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
