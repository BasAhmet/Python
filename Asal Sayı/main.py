def asallariBulma(baslangicSayisi,bitisSayisi):
    from math import sqrt
    asallar = []
    if baslangicSayisi < 3:
        asallar.append(2)
        baslangicSayisi = 3
    if baslangicSayisi % 2 == 0:
        baslangicSayisi += 1
    for i in range(baslangicSayisi,bitisSayisi+1,2):
        asal = True
        for j in range (2,int(sqrt(i))+1):
            if i % j == 0:
                asal = False
        if asal:
            asallar.append(i)
    print(asallar)
def asalmi(sayi):
    from math import sqrt
    asal = True
    if sayi == 2:
        print(f"{sayi} sayısı asal sayıdır.")
    else:
        for i in range(2,int(sqrt(sayi))+2):
            if sayi % i == 0:
                print(f"{sayi} sayısı {i} sayısına tam bölünüyor. Asal değildir.")
                asal = False
                break
        if asal:
            print(f"{sayi} sayısı asal sayıdır.")
while True:
    print('''
*********************** MENÜ ***********************
Bir sayı asal mı diye sorgulamak için            : 1
İstediğiniz aralıktaki asal sayıları bulmak için : 2
Çıkmak için                                      : 3
****************************************************''')
    islem = input("\nHangi İşlemi Yapmak İstersiniz : ")
    if islem == "1":
        sayi = int(input("Lütfen bir sayı giriniz : "))
        asalmi(sayi)
    elif islem == "2":
        baslangicSayisi = int(input("\nLütfen bir başlangıç sayısı giriniz : "))
        bitisSayisi = int(input("Lütfen bir bitiş sayısı giriniz     : "))
        if baslangicSayisi < bitisSayisi:
            asallariBulma(baslangicSayisi,bitisSayisi)
        elif baslangicSayisi >= bitisSayisi:
            print("Başlangıç sayısı bitiş sayısından küçük olmalı.\nMenüye dönüş yapıldı.")
    elif islem == "3":
        print("Çıkış işlemi gerçekleşti.")
        break