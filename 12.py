# Bir değişken, yalnızca oluşturulduğu bölgenin içinden kullanılabilir. Buna kapsam denir .
# Bir fonksiyonun içinde oluşturulan bir değişken , o fonksiyonun yerel kapsamına aittir ve sadece o fonksiyonun içinde kullanılabilir.

# Genel bir değişken oluşturmanız gerekiyorsa, ancak yerel kapsamda sıkışıp kaldıysanız, globalanahtar kelimeyi kullanabilirsiniz.
# Ayrıca, globalbir işlev içindeki genel bir değişkende değişiklik yapmak istiyorsanız anahtar kelimeyi kullanın.
import json
import datetime
import platform
x = 300


def myFunc():
    global x
    x = 10


myFunc()
print(x)

# Anahtar kelimeyi kullanarak bir modülü içe aktardığınızda bir takma ad oluşturabilirsiniz as
# import module as mx gibi

# Python'da istediğiniz zaman içe aktarabileceğiniz birkaç yerleşik modül vardır.

# Bir modüldeki tüm işlev adlarını (veya değişken adlarını) listelemek için yerleşik bir işlev vardır. dir()fonksiyon
x = dir(platform)
print(x)

# Python'da bir tarih kendi başına bir veri türü değildir, ancak datetimetarihlerle çalışmak için adlandırılmış bir modülü tarih nesneleri olarak içe aktarabiliriz.
x = datetime.datetime.now()
print(x)
# Yılı ve haftanın gününün adını döndürür:
print(x.year)
print(x.strftime("%A"))

# İşlev abs(), belirtilen sayının mutlak (pozitif) değerini döndürür:
x = abs(-7.25)
print(x)

# İşlev , x'in değerini y'nin (x^y ) gücüne döndürür.pow(x, y)
# Python ayrıca mathmatematiksel işlevlerin listesini genişleten yerleşik bir modüle sahiptir.
# Kullanmak için mathmodülü içe aktarmalısınız
# import math


# Bir JSON dizeniz varsa, json.loads()yöntemi kullanarak onu ayrıştırabilirsiniz.
# Bir Python nesneniz varsa, json.dumps()yöntemi kullanarak onu bir JSON dizesine dönüştürebilirsiniz.

# indentGirinti sayısını tanımlamak için parametreyi kullanın

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# separatorsVarsayılan ayırıcıyı değiştirmek için parametreyi kullanın :
print(json.dumps(x, indent=4, separators=(". ", " = ")))
