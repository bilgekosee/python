# Varyans, değerlerin ne kadar dağıldığını gösteren başka bir sayıdır.
# Standart Sapma genellikle Sigma sembolü ile temsil edilir: σ
# Varyans genellikle Sigma Kare sembolü ile temsil edilir: σ 2
import numpy

speed = [32, 111, 138, 28, 32, 32, 32, 59, 77, 97]

x = numpy.var(speed)
print(x)


# Yüzdelikler, istatistiklerde, değerlerin belirli bir yüzdesinin altında olduğu değeri açıklayan bir sayı vermek için kullanılır.
# percentile()Yüzdelikleri bulmak için NumPy yöntemini kullanın :

y = numpy.percentile(speed, 32)
print(y)
