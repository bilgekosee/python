print("hello world")
"""
Girinti, bir kod satırının başındaki boşlukları ifade eder.
Diğer programlama dillerinde koddaki girinti yalnızca okunabilirlik içindir, Python'daki girinti çok önemlidir.
Python, bir kod bloğunu belirtmek için girinti kullanır.
Aynı kod bloğunda aynı sayıda boşluk kullanmanız gerekir, aksi takdirde Python size bir hata verir
"""

if 5 > 2:
    print("beş ikiden büyüktür")

a = 5
b = "hellööö bilge"
print(a)
print(b)

# tekli yorum satırı

# type()Fonksiyon ile bir değişkenin veri tipini alabilirsiniz
print(type(a))
print(type(b))

# Python, bir satırda birden çok değişkene değer atamanıza izin verir:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Aynı değer tek bir satırda birden çok değişkene atayabilirsiniz :
d = e = f = "bilge"
print(d)
print(e)
print(f)

# Bir listede değerler toplamınız varsa, Tuple vb. Python, değerleri değişkenlere çıkarmanıza izin verir. Buna paket açma denir .

fruits = ["a", "b", "c"]
g, h, w = fruits
print(g)
print(h)
print(w)
