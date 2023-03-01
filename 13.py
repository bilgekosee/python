# RegEx, bir dizenin belirtilen arama modelini içerip içermediğini kontrol etmek için kullanılabilir.
# import re şeklinde

# cümlenin the ile başlayıp spain ile bitip bitmediğini kontrol etme
import re
txt = "the rain in spain"
x = re.search("^the.*spain$", txt)
if x:
    print("yes")
else:
    print("no")

# İşlev sub(), eşleşmeleri seçtiğiniz metinle değiştirir:
x = re.sub("\s", "9", txt)
print(x)


# PIP, Python paketleri veya isterseniz modüller için bir paket yöneticisidir.

# Blok try, hatalar için bir kod bloğunu test etmenizi sağlar.
# Blok except, hatayı işlemenizi sağlar.
# Blok else, hata olmadığında kod yürütmenizi sağlar.
# Blok finally, try- ve hariç tutma bloklarının sonucundan bağımsız olarak kod yürütmenizi sağlar.
# Blok finally, belirtilirse, try bloğunun bir hata oluşturup oluşturmadığına bakılmaksızın yürütülür.


# Bir dizginin beklendiği gibi görüntülendiğinden emin olmak için, yöntemi kullanarak sonucu biçimlendirebiliriz format().
f = open("python.txt", "r")
print(f.read())

# Python'da yeni bir dosya oluşturmak için open()aşağıdaki parametrelerden biriyle yöntemi kullanın:
# "x"- Oluştur - yeni bir dosya oluşturur, dosya varsa bir hata döndürür
# "a"- Ekle - belirtilen dosya yoksa bir dosya oluşturur
# "w"- Yaz - belirtilen dosya yoksa bir dosya oluşturur
