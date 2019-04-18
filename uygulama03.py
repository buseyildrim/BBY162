"""
18.04.2019
Buse Yıldırım
Uygulama03
Hocam random modülü hata verdiği için ödevimi gününde yapamadım, hem de konuyu tam kavrayıp benimseyerek yapmak istedim ve tamamen anladım.
Basit bir adam asmaca yaptıktan sonra bunu basit bularak sözlük gibi kavramlar ile geliştirdim.
"""

print("♥","♥","♥")
print("Dünyanın en büyük 5 ülkesinin başkentlerini biliyor musun?")
print("**** Adam asmaca ****")
import random

kelimeListesi=("Pekin","Delhi", "Washington", "Cakarta", "Brasilia")
sözlük={"Pekin":"Çin'in Başkentidir",
        "Delhi":"Hindistanın Başkentidir.",
        "Washington":"ABD Başkentidir.",
        "Cakarta":"Endonezyanın başkentidir.",
        "Brasilia":"Brezilyanın Başkentidir."}


kelimeListesi=random.choice(["Pekin","Delhi", "Washington", "Cakarta", "Brasilia"])
kelimeListesi = kelimeListesi.upper()
canSayisi = 3
kelimeler = []

if kelimeler== "Pekin":
    print(sözlük["pekin"])
if kelimeler== "Delhi":
    print(sözlük["Delhi"])
if kelimeler=="Washington":
    print(sözlük["washington"])
if kelimeler=="cakarta":
    print(sözlük["cakarta"])
if kelimeler=="Brasilia":
    print(sözlük["Brasilia"])


for word in kelimeListesi:

    kelimeler.append("_")
    harfSayisi = "_"

print(kelimeler)
while canSayisi > 0:

    can = 0
    tahmin = input("bir harf girin: ")
    tahmin = tahmin.upper()

    if tahmin in kelimeListesi:
        for kontrol in kelimeListesi:
            if kelimeListesi[can] == tahmin:
                kelimeler[can] = tahmin
            can += 1

        print("")
        print(kelimeler)
        print("\"%s\" harfi " %tahmin)

    else:
        canSayisi -= 1
        print("")
        print(kelimeler)
        print("\"%s\" harfi yanlış. Başka harf girin" % tahmin)
        print(canSayisi, "Canınız Kaldı")

    if canSayisi == 0:
        print('Maalesef bilemediniz!Doğru kelime "{}"'.format(kelimeListesi))
        break


    if harfSayisi not in kelimeler:
        print("Tebrikler! Doğru tahmin")
        break
input()
