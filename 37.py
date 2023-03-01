import matplotlib.pyplot as plt
import numpy

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# NumPy'nin bir polinom modeli yapmamızı sağlayan bir yöntemi var
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Ardından satırın nasıl görüneceğini belirtin, 1. konumdan başlayıp 22. konumda bitirelim
myline = numpy.linspace(1, 22, 100)


plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# x ve y ekseni değerleri arasındaki ilişkinin ne kadar iyi olduğunu bilmek önemlidir, eğer ilişki yoksa polinom regresyon hiçbir şeyi tahmin etmek için kullanılamaz.
