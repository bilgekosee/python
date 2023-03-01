# Bir lambda işlevi herhangi bir sayıda bağımsız değişken alabilir, ancak yalnızca bir ifadeye sahip olabilir.
def x(a): return a+10


print(x(5))

# Lambda'nın gücü, onları başka bir işlev içinde anonim bir işlev olarak kullandığınızda daha iyi gösterilir.
# Diyelim ki bir bağımsız değişken alan bir işlev tanımınız var ve bu bağımsız değişken bilinmeyen bir sayıyla çarpılacak
# Gönderdiğiniz sayıyı her zaman ikiye katlayan bir işlev yapmak için bu işlev tanımını kullanın


def function(n):
    return lambda a: a*n


mydoubler = function(2)
print(mydoubler(11))


# Sınıfların anlamını anlamak için yerleşik __init__() işlevini anlamamız gerekir.
# Tüm sınıflar, her zaman sınıf başlatıldığında yürütülen __init__() adlı bir işleve sahiptir.
# Nesne özelliklerine veya nesne oluşturulurken yapılması gereken diğer işlemlere değer atamak için __init__() işlevini kullanın

# __str__() işlevi, sınıf nesnesi bir dize olarak temsil edildiğinde neyin döndürüleceğini kontrol eder.
# __str__() işlevi ayarlanmamışsa, nesnenin dize gösterimi döndürülür
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)
# Parametre self, sınıfın geçerli örneğine bir referanstır ve sınıfa ait değişkenlere erişmek için kullanılır.
# Adlandırılmış olması gerekmez self, onu istediğiniz gibi adlandırabilirsiniz, ancak sınıftaki herhangi bir işlevin ilk parametresi olması gerekir:


# İşlevselliği başka bir sınıftan devralan bir sınıf oluşturmak için, alt sınıfı oluştururken üst sınıfı bir parametre olarak gönderin
# StudentSınıfın özelliklerini ve yöntemlerini devralacak adında bir sınıf oluşturun Person
class Student(Person):
    pass
# Artık Student sınıfı, Person sınıfıyla aynı özelliklere ve yöntemlere sahiptir.


# Python ayrıca, super()alt sınıfın ebeveyninden tüm yöntemleri ve özellikleri devralmasını sağlayacak bir işleve sahiptir
"""class Student(Person):
 def __init__(self, fname, lname):
   super().__init__(fname, lname)"""
# İşlevi kullandığınızda super(), ana öğenin adını kullanmanız gerekmez, otomatik olarak üst öğesinden yöntemleri ve özellikleri devralır.


# Teknik olarak, Python'da bir yineleyici, yöntemlerden oluşan yineleyici protokolünü uygulayan bir nesnedir __iter__() ve __next__().
# Bir demetten bir yineleyici döndürün ve her değeri yazdırın:
mytuple = ("anne", "baba", "çocuk")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Yinelemenin sonsuza kadar devam etmesini önlemek için StopIterationifadeyi kullanabiliriz.


class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = Mynumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
