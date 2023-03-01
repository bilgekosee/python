txt = "the best things in life are free!"
if "free" in txt:
    print("yes , 'free' is present")

# Belirli bir ifadenin veya karakterin bir dizide OLMADIĞINI kontrol etmek için anahtar kelimeyi kullanabiliriz not in.
text = "i pray the lord my soul to keep"
print("love" not in text)
# Dilim sözdizimini kullanarak bir dizi karakter döndürebilirsiniz.
# Dizenin bir bölümünü döndürmek için başlangıç ​​dizinini ve bitiş dizinini iki nokta üst üste ile ayırarak belirtin.

b = "hello world"
print(b[3:6])
# Karakterleri 3. konumdan 6. konuma getirin (dahil değildir):


# Dilimi dizenin sonundan başlatmak için negatif dizinler kullanın:
print(b[-5:-2])

# Yöntem upper(), dizeyi büyük harfle döndürür
a = "  biLge  "
print(a.upper())
# Yöntem lower(), dizeyi küçük harfle döndürür
print(a.lower())


# Boşluk, gerçek metinden önceki ve/veya sonraki boşluktur ve çoğu zaman bu boşluğu kaldırmak istersiniz
print(a.strip())
# replace(), bir dizeyi başka bir dizeyle değiştirir
print(a.replace("b", "r"))

# split(), belirtilen ayırıcı arasındaki metnin liste öğeleri haline geldiği bir liste döndürür
x = "hello,my,friends"
print(x.split(","))
