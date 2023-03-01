# İşlevde print(), virgülle ayırarak birden çok değişken çıktısı alırsınız:
import random
x = "python"
y = "is"
z = "awasome"
print(x, y, z)
# Birden fazla değişkenin çıktısını almak için + operatörü de kullanabilirsiniz
# print(x+y+z)

# Bir fonksiyonun dışında bir değişken oluşturun ve onu fonksiyonun içinde kullanın


def myfunc():
    z = "bad"
    print("python is " + z)


myfunc()
# Bir fonksiyon içerisinde aynı isimde bir değişken oluşturursanız, bu değişken yerel olur ve sadece fonksiyon içerisinde kullanılabilir. Aynı ada sahip global değişken, olduğu gibi, global ve orijinal değeri ile kalacaktır.
print("python is " + z)

# Ayrıca, globalbir fonksiyonun içindeki global bir değişkeni değiştirmek istiyorsanız, anahtar kelimeyi kullanın.
a = "mercy"


def myFunc():
    global a
    a = "not mercy"


myFunc()

print("python is " + a)


# int(), float()ve complex()yöntemleri kullanarak bir türden diğerine dönüştürebilirsiniz :
w = 1
e = 2.9
r = 1j  # Not: Karmaşık sayıları başka bir sayı türüne dönüştüremezsiniz.

q = float(w)
t = int(e)
u = complex(w)

print(q)
print(t)
print(u)

print(type(q))
print(type(t))
print(type(u))

# Python'un rasgele sayı yapma işlevi yoktur, ancak Python'un rasgele sayılar yapmak için kullanılabilecek random()yerleşik bir modülü vardır:random

print(random.randrange(1, 10))

# Üç tırnak kullanarak bir değişkene çok satırlı bir dize atayabilirsiniz:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

"""
Diğer birçok popüler programlama dili gibi, Python'daki dizeler de unicode karakterleri temsil eden bayt dizileridir.
Bununla birlikte, Python'un bir karakter veri türü yoktur, tek bir karakter yalnızca 1 uzunluğunda bir dizedir.
Dizenin öğelerine erişmek için köşeli parantezler kullanılabilir.
"""
m = "hello bilge"
print(m[2])

# Dizeler dizi olduğundan, bir dizedeki karakterler arasında bir fordöngü ile döngü yapabiliriz.
for v in "fıkıfıkı":
    print(v)

# Bir dizenin uzunluğunu almak için len()işlevi kullanın.
n = "fıkıfıkı pikacuu"
print(len(n))
