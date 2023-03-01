# listenin bir kopyasını oluşturun copy()
thislist = ["mit", "ucla", "harvard"]
mylist = thislist.copy()
print(mylist)
# Bir kopya oluşturmanın başka bir yolu da yerleşik yöntemi kullanmaktır list()
mylist = list(thislist)
print(mylist)

# Python'da iki veya daha fazla listeyi birleştirmenin veya birleştirmenin birkaç yolu vardır.
# En kolay yollardan biri + operatörü kullanmaktır.

list1 = ["a", "b", "c"]
list2 = [0, 1, 2, 3]
list3 = list1+list2
print(list3)

# İki listeyi birleştirmenin başka bir yolu, list2'deki tüm öğeleri liste1'e teker teker eklemektir
for x in list2:
    list1.append(x)
print(list1)

# extend() Ya da amacı bir listeden başka bir listeye öğe eklemek olan yöntemi kullanabilirsiniz
list1.extend(list2)
print(list1)

# Demetler, birden çok öğeyi tek bir değişkende depolamak için kullanılır.
# Tuple, Python'da veri koleksiyonlarını depolamak için kullanılan 4 yerleşik veri türünden biridir, diğer 3'ü List , Set ve Dictionary olup , tümü farklı niteliklere ve kullanıma sahiptir.
# Tuple, sıralı ve değiştirilemez bir koleksiyondur .

thistuple = ("tokyo", "osaka", "nara")
print(thistuple)
# Demetlerin sıralı olduğunu söylediğimizde, bu, öğelerin tanımlanmış bir sırası olduğu ve bu sıranın değişmeyeceği anlamına gelir.
# Demetler değiştirilemez, yani demet oluşturulduktan sonra öğeleri değiştiremez, ekleyemez veya kaldıramayız.

# Bir öğe demeti, virgülü unutmayın
thistup = ("a",)
print(type(thistup))
thistupl = ("b")
print(type(thistupl))

# Bir demet oluşturmak için tuple() yapıcısını kullanmak da mümkündü
tuple1 = tuple(("apple", "mango"))
print(tuple1)


# biliyoruz ki Bir demet oluşturulduktan sonra değerlerini değiştiremezsiniz. Demetler değiştirilemez veya aynı zamanda adlandırıldığı şekliyle değişmezdir .
# Ama geçici bir çözüm var. Tuple'ı bir listeye dönüştürebilir, listeyi değiştirebilir ve listeyi tekrar bir Tuple'a dönüştürebilirsiniz
x = ("bugatti", "ferrari", "mercedes")
y = list(x)
y[1] = "lexus"
x = tuple(y)
print(x)

renk = ("mavi", "gri", "siyah")
r = list(renk)
r[2] = "turuncu"
renk = tuple(r)
print(renk)

# Bir demete demet ekleyin . Demetlere demet eklemenize izin verilir, bu nedenle bir (veya daha fazla) öğe eklemek istiyorsanız, öğelerle yeni bir demet oluşturun ve onu mevcut demete ekleyin:
a = ("sarı",)
renk += a
print(renk)
# Yalnızca bir öğe içeren bir demet oluştururken, öğeden sonra virgül koymayı unutmayın, aksi halde bir demet olarak tanımlanmayacaktır

# Bir demetteki öğeleri kaldıramazsınız.ama ekleme ve dğiştirmede olduğu gibi list e çevirip kaldırabiliyoruz
r.remove("gri")
renk = tuple(r)
print(renk)
# Veya demeti tamamen silebilirsiniz
del renk
print(renk)
