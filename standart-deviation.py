# Standart sapma, değerlerin nasıl dağıldığını açıklayan bir sayıdır.
# Düşük bir standart sapma, sayıların çoğunun ortalama (ortalama) değere yakın olduğu anlamına gelir.
# Yüksek bir standart sapma, değerlerin daha geniş bir aralığa dağıldığı anlamına gelir.

import numpy
speed = [86, 87, 88, 86, 87, 85, 86]

x = numpy.std(speed)
print(x)
