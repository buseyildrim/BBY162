#Buse Yıldırım
#comment1

metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[ :20])

#comment2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık veri", "Açık Kültür"]

for i in liste:
    print(i)

#comment3
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
kelime=[]

sozluk=input("Öğrenmek istediğiniz kelimeyi giriniz!")
cevap = input("kelime:")
cevap = cevap.input() 
if cevap in sozluk:
    print(sozluk[cevap])
else:
    print("kelime bulunamadı!!")
        
