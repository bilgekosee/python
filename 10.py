# "Muz" kelimesindeki harfler arasında dolaşın:
for a in "muz":
    print(a)

# Bir kod kümesinde belirli sayıda döngü yapmak için range() işlevini kullanabiliriz,
# range() işlevi , varsayılan olarak 0'dan başlayan ve (varsayılan olarak) 1 artan bir sayı dizisi döndürür ve belirtilen bir sayıda biter.
for b in range(5):
    print(b)
# range() işlevi varsayılan olarak diziyi 1 artırır, ancak üçüncü bir parametre ekleyerek artış değerini belirtmek mümkündür: range(2, 30, 3 ) :
for z in range(2, 18, 4):
    print(z)
# Her meyve için her sıfatı yazdırın:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# pythonda fonsiyon def ile çağırılır


def my_function():
    print("hello from a function")


my_function()

# Varsayılan olarak, bir işlev doğru sayıda bağımsız değişkenle çağrılmalıdır. Yani, işleviniz 2 argüman bekliyorsa, işlevi 2 argümanla çağırmalısınız, daha fazla veya daha az değil.


def myfunc(fname, lname):
    print(fname+" " + lname)


myfunc("emil0", "refsnes")


# İşlevinize kaç bağımsız değişkenin iletileceğini bilmiyorsanız *, işlev tanımında parametre adından önce bir ekleyin.
def function(*singer):
    print("the best singer is  " + singer[2])


function("alofur", "tamino", "amber run")


# İşlevinize kaç tane anahtar sözcük bağımsız değişkeninin aktarılacağını bilmiyorsanız **, işlev tanımında parametre adından önce iki yıldız işareti: ekleyin.
def my(**kid):
    print("his last name is " + kid["rname"])


my(ename="tobias", rname="refness")

# İşlevi bağımsız değişken olmadan çağırırsak, varsayılan değeri kullanır:


def my_function1(country="Norway"):
    print("I am from " + country)


my_function1("Sweden")
my_function1("India")
my_function1()
my_function1("Brazil")

# özyinelemeyi anlamadım


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
