# dictionary veri değerlerini anahtar:değer çiftlerinde depolamak için kullanılır.
# dictionary  sıralı*, değişken ve tekrara izin vermeyen bir koleksiyondur.
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "colors": ["red", "black", "yellow"]
}
print(thisdict)

# Sözlüklerin sıralı olduğunu söylediğimizde, maddelerin belirli bir sırası olduğu ve bu sıralamanın değişmeyeceği anlamına gelir.
# Sırasız, öğelerin tanımlanmış bir sırası olmadığı anlamına gelir, bir öğeye bir dizin kullanarak başvuramazsınız.
# Sözlükler değiştirilebilir, yani sözlük oluşturulduktan sonra öğeleri değiştirebilir, ekleyebilir veya kaldırabiliriz.
x = thisdict["model"]
print(x)
# "Model" anahtarının değerini get() ile alın
y = thisdict.get("model")
print(y)

# Yöntem keys(), sözlükteki tüm anahtarların bir listesini döndürür.
a = thisdict.keys()
print(a)

# values(), sözlükteki tüm değerlerin bir listesini döndürür.
b = thisdict.values()
print(b)

# items(), bir sözlükteki her öğeyi bir listedeki demetler olarak döndürür.
c = thisdict.items()
print(c)

if "model" in thisdict:
    print("yes model is one of the keys in the disdict dictionary")

# Yöntem update(), sözlüğü verilen bağımsız değişkendeki öğelerle güncelleyecektir.
thisdict.update({"year": 2000})
print(thisdict)

# Yöntemi kullanarak hem anahtarlar hem de değerler arasında geçiş yapın:items()
for q, w in thisdict.items():
    print(q, w)

# Bir sözlük sözlükler içerebilir, buna iç içe geçmiş sözlükler denir.
myfamily = {
    "child1": {
        "name": "jessica",
        "year": 2024
    },
    "child2": {
        "name": "saturn",
        "year": 2030

    },
    "child3": {
        "name": "justin",
        "year": 1999
    }
}
print(myfamily)

# Yürütülecek tek bir ifadeniz varsa, bunu if ifadesiyle aynı satıra koyabilirsiniz.
v = 2
n = 7
if v > n:
    print("v is greater than n")
else:
    print("önceki sav doğr değil")

# While döngüsü ile, bir koşul doğru olduğu sürece bir dizi ifade çalıştırabiliriz.
i = 1
while i < 7:
    print(i)
    i += 1
# Break deyimi ile while koşulu doğru olsa bile döngüyü durdurabiliriz:
l = 1
while l < 9:
    print(l)
    if l == 3:
        break
    l += 1
# Devam deyimi ile mevcut yinelemeyi durdurabilir ve bir sonraki ile devam edebiliriz :
    if l == 4:
        continue
    print(l)
