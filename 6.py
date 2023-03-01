# Ayrıca dizin numaralarına bakarak liste öğeleri arasında geçiş yapabilirsiniz.
# Uygun bir yineleme oluşturmak için range()ve işlevlerini kullanın len()
thislist = ["mert", "ediz", "poyraz"]
for i in range(len(thislist)):
    print(thislist[i])

# Bir döngü kullanarak liste öğeleri arasında geçiş yapabilirsiniz while.
# Listenin uzunluğunu belirlemek için işlevi kullanın len(), ardından 0'dan başlayın ve dizinlerine başvurarak liste öğeleri arasında dolaşın.
# Her yinelemeden sonra dizini 1 artırmayı unutmayın.

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

# Bir meyve listesine göre, yalnızca adında "a" harfi bulunan meyveleri içeren yeni bir liste istiyorsunuz.
# forListeyi anlamadan, içinde koşullu bir test olan bir ifade yazmanız gerekecek
fruits = ["apple", "banana", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# range()Bir yinelenebilir oluşturmak için işlevi kullanabilirsiniz
newlist = [x for x in range(10)]
print(newlist)
# Aynı örnek, ancak bir koşulla
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)
# Yeni listedeki tüm değerleri 'merhaba' olarak ayarlayın
newlist = ['hello' for x in fruits]
print(newlist)

felsefe = ["EPIKTATOS", "MARK TWAIN", "SENECA"]
list = []
for y in felsefe:
    if "a" in y:
        list.append(y)
print(list)

list = [y.lower() for y in felsefe]
print(list)


# Liste nesnelerinin sort(), listeyi varsayılan olarak artan şekilde alfabetik olarak sıralayacak bir yöntemi vardır:
list1 = ["Carolyn", "diana", "bojack", "Todd"]
list1.sort()
print(list1)
# bu sayılar için deyazılabilir

# Azalan sıralama için, anahtar kelime bağımsız değişkenini kullanın reverse = True
list1.sort(reverse=True)
print(list1)

# Argüman anahtar sözcüğünü kullanarak kendi işlevinizi de özelleştirebilirsiniz .key = function
# İşlev, listeyi sıralamak için kullanılacak bir sayı döndürür (önce en düşük sayı)

# sayının 50 ye ne kadar yakın olduğuna göre sıraladum


def myFunc(n):
    return abs(n-50)


list2 = [10, 98, 36, 85, 62]
list2.sort(key=myFunc)
print(list2)

# sort büyük küçük harfe duyarlıdır sıralamayı değiştirir
# büyük/küçük harfe duyarsız bir sıralama işlevi istiyorsanız, anahtar işlev olarak str.lower'ı kullanın:
list1.sort(key=str.lower)
print(list1)

# Alfabeden bağımsız olarak bir listenin sırasını tersine çevirmek isterseniz ne olur?
# Yöntem reverse(), öğelerin geçerli sıralama düzenini tersine çevirir.

list1.reverse()
print(list1)
