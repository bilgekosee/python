# Doğrusal regresyon, veri noktaları arasındaki ilişkiyi, hepsi boyunca düz bir çizgi çizmek için kullanılır
# Bu çizgi gelecekteki değerleri tahmin etmek için kullanılabilir.Makine Öğreniminde geleceği tahmin etmek çok önemlidir.


from scipy import stats
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# Yeni bir değer döndürmek için slopeve değerlerini kullanan bir işlev oluşturun . interceptBu yeni değer, karşılık gelen x değerinin y ekseninde nereye yerleştirileceğini temsil eder


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)  # Orijinal dağılım grafiği
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
