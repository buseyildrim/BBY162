"""
Python ödev 2
Buse Yıldırım
"""
print("*** Merhaba, mini bir genel kültür testine ne dersin? ***")
print("Aşağıdakilerden hangisi doğrudur? ")
print("-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-")
sorular = ["Ankara ne zaman başkent olmuştur?",\
           "Atların insanlardan ne kadar fazla kemiği vardır ? ",\
           "Mavi rengi görebilen tek kuş türü nedir? ",\
           "Gözü beyninden küçük olan canlı hangisidir?",\
           "Aşağıdakilerden hangisi kendilerine özgü parmak izi olan canlılardan değildir?",]

cevaplar = ["A","B", "A", "C", "D"]
cevapA =["1923", "17", "Baykuş", "Maymun", "Koalalar" ]
cevapB =["1919", "18", "Yarasa", "Ördek", "Primatlar"]
cevapC =["1933", "30", "Akbaba", "Devekuşu", "İnsanlar"]
cevapD =["1932", "18", "Papağan","İnsan","Hayvanlar"]
puan =0
for i in range (len(sorular)):
    print("soru " + str(i+1)+":"+sorular[i])
    print("A: " + cevapA[i])
    print("B: " + cevapB[i])
    print("C: " + cevapC[i])
    print("D: " + cevapD[i])
    cevap = input("cevabınızı giriniz: ")
    if cevaplar[i] == cevap.upper():
       puan +=1
print("Testin sonuna geldiniz. Eğer puanınız 0-50 aralığında ise genel kültür seviyenizi tekrar gözden geçirmelisiniz. 50 ve üstü puanlar için Tebrikler!")
print("Aldığınız not: "+ str(int((puan/len(sorular))*100)))




