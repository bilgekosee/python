# İki diziyi birleştirmek veya birleştirmek için + operatörünü kullanabilirsiniz.
a = "hello"
b = "world"
#c = a + b
# print(c)
# Aralarına boşluk eklemek için şunu ekleyin " "
c = a + " " + b
print(c)

# format()Dizelere sayı eklemek için yöntem
age = 25
txt = "his name is justin, and you are {}"
print(txt.format(age))

# sınırsız sayıda değişken alabilir format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Bir dizgede geçersiz olan karakterleri eklemek için bir kaçış karakteri kullanın.
# Bir kaçış karakteri, \ardından eklemek istediğiniz karakterin geldiği bir ters eğik çizgidir.
# Geçersiz karaktere bir örnek, çift tırnak içine alınmış bir dize içindeki çift tırnaktır:

text = "we are so-called \"vikings\" from the north"
print(text)

# Bir if ifadesinde bir koşul çalıştırdığınızda, Python Trueveya döndürür False:
q = 200
e = 33
if q > e:
    print("e is greater q")
else:
    print("e is not greater q")

 # bir değer veya nesne daha olarak değerlendirilir ve bu, veya döndüren Falsebir işleve sahip bir sınıftan yapılmış bir nesneye sahip olmanızdır :__len__0False


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Bir Boole Değeri döndüren işlevler oluşturabilirsiniz:
def myFonction():
    return True


print(myFonction())
