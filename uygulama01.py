"""
Python ödev 1
"Bunları biliyor musun?"
Buse Yıldırım
"""
print("*** Merhaba, Bunları biliyor musun? ***")
print("Aşağıdaki sorulara 'D' ya da 'E' ile cevap ver! ")
print("------------------------------------------------")
sorular = ["Salatalık bir meyve değil, sebze\'dir[D/Y]",\
           "Atların insanlardan 18 tane fazla kemiği vardır[D/Y]",\
           "Baykuş mavi rengi görebilen tek kuştur.[D/Y]",\
           "Bir devekuşunun gözü beyninden küçüktür.[D/Y]",\
           "Koalalar, primatlar ve insanlar, kendilerine özgü parmak izi olan tek canlılardır[D/Y]",]
cevaplar = ["Y", "D", "D", "Y","D"]
puan = 0

#soru1
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("Tebrikler! Cevap doğru.")
    puan +=1
else:
    print("Cevabınız yanlış! Salatalık bir meyvedir.")

#soru2
cevap = input((sorular[1]))
if cevaplar [1] == cevap.upper():
    print("Tebrikler! Cevap doğru.")
    puan +=1
else:
    print("Cevabınız yanlış! Atların insanlardan 18 tane fazla kemiği vardır.")
#soru3
cevap = input((sorular[2]))
if cevaplar [2] == cevap.upper():
    print("Tebrikler! Cevap doğru.")
    puan +=1
else:
    print("Cevabınız yanlış! Mavi rengi görebilen tek kuş baykuştur.")

#soru4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Tebrikler! Cevap doğru.")
    puan +=1
else:
    print("Cevabınız yanlış !Bir devekuşunun gözü beyninden büyüktür.")

#soru5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Tebrikler! Cevap doğru.")
    puan +=1
else:
    print("Cevabınız yanlış!")


#test Sonu
print("Testi tamamladınız, aldığınız not: "+str(puan*20))





