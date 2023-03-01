# Listelerin sıralı olduğunu söylediğimizde, maddelerin belirli bir sırası olduğu ve bu sıralamanın değişmeyeceği anlamına gelir.
# Bir listeye yeni öğeler eklerseniz, yeni öğeler listenin sonuna yerleştirilir.

# Bir listenin kaç öğeye sahip olduğunu belirlemek için şu len()işlevi kullanın:
thislist = ["a", "b", "c"]
print(len(thislist))

# Bir liste farklı veri türleri içerebilir
# Python'un bakış açısından listeler, 'liste' veri tipine sahip nesneler olarak tanımlanır:
# <class 'list'>

mylist = ["apple", "banana", "cherry"]

print(type(mylist))
# Arama dizin 2'de (dahil) başlayacak ve dizin 5'te (dahil değil) sona erecektir.
thislistt = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislistt[2:5])

# Mevcut değerlerden herhangi birini değiştirmeden yeni bir liste öğesi eklemek için insert()yöntemi kullanabiliriz
kume = ["adele", "one ok rock", "lil nas"]
kume.insert(2, "black pumas")
print(kume)

# Listenin sonuna bir öğe eklemek için append() yöntemini kullanın
kume.append("bob marley")
print(kume)

# Geçerli listeye başka bir listeden öğeler eklemek için extend()yöntemi kullanın
tropical = ["mango", "pineapple"]
kume.extend(tropical)
print(kume)
# remove(), belirtilen öğeyi kaldırır.
kume.remove("lil nas")
print(kume)
# pop(), belirtilen dizini kaldırır.
kume.pop(1)
print(kume)
# Dizini belirtmezseniz, pop()yöntem son öğeyi kaldırır.
kume.pop()
print(kume)
# delkelime ayrıca listeyi tamamen silebilir.
thisislist = ["moon", "sun"]
del thisislist

# Yöntem clear()listeyi boşaltır.
# Liste hala duruyor, ancak içeriği yok.
thisilist = ["stand", "by", "me"]
thisilist.clear()
print(thisilist)
