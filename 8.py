# Python'da, değerleri tekrar değişkenlere çıkarmamıza da izin verilir. Buna "ambalajdan çıkarma" denir:
fruits = ("apple", "mango", "kiwi")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Değişken sayısı, kayıt defterindeki değer sayısıyla eşleşmelidir, değilse, kalan değerleri bir liste olarak toplamak için yıldız işareti kullanmalısınız
fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")

(greenn, yelloww, *redd) = fruit

print(greenn)
print(yelloww)
print(redd)

# Bir demetin içeriğini belirli sayıda çarpmak istiyorsanız, * operatörü kullanabilirsiniz:
mytuple = fruit*2
print(mytuple)


# Set öğeleri değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.
# Kümeler süslü parantezlerle yazılır.

thisset = {"geçmiş", "şimdi", "gelecek"}
print(thisset)
# Kümeler sırasızdır, dolayısıyla öğelerin hangi sırada görüneceğinden emin olamazsınız.

# Kümeler aynı değere sahip iki öğeye sahip olamaz.mesela gelecekten bir tane daha olsaydı bile tek bir tanesi gözükecekti
# sette geçmiş olup olmadığını arayın
print("geçmiş" in thisset)

# Bir kümeye bir öğe eklemek için add() yöntemi kullanın.
thisset.add("hiçlik")
print(thisset)

# Geçerli kümeye başka bir kümeden öğeler eklemek için update() yöntemi kullanın.
tropical = {"mango", "kiwi", "ebesinin nikahı"}
thisset.update(tropical)
print(thisset)
# Kümedeki bir öğeyi kaldırmak için remove(), veya discard()yöntemini kullanın.
thisset.remove("ebesinin nikahı")
print(thisset)

# Yöntemi bir öğeyi kaldırmak için de kullanabilirsiniz , ancak bu yöntem son öğeyi pop()kaldıracaktır . Setlerin sırasız olduğunu unutmayın, dolayısıyla hangi öğenin kaldırılacağını bilemezsiniz.
thisset.pop()
print(thisset)
# Kümeler sırasızdır , bu nedenle pop()yöntemi kullanırken hangi öğenin kaldırılacağını bilemezsiniz.

# Her union()iki kümedeki tüm öğeleri içeren yeni bir küme döndüren yöntemi veya update()bir kümedeki tüm öğeleri diğerine ekleyen yöntemi kullanabilirsiniz:
set1 = {"a", "b", "x"}
set2 = {"q", "p", "z", "a"}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set3)

# Yöntem intersection_update(), yalnızca her iki kümede de bulunan öğeleri tutacaktır.
set1.intersection_update(set2)
print(set1)

# Yöntem , yalnızca her iki kümede de bulunan öğeleri içeren yeniintersection() bir küme döndürür
x = {"iphone", "huawei", "samsung", "apple"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# symmetric_difference_update(), yalnızca her iki kümede de mevcut OLMAYAN öğeleri tutacaktır.
x.symmetric_difference_update(y)
print(x)
