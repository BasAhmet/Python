def sayiHarfSayar(sayi = 999):
    basamaklar = [[""],
    ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"], # Birler basamağı
    ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"], # Onlar basamağı
    ["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"], # Yüzler basamağı
    ["","bin"]] # Binler basamağı
    toplam = 0
# Fonksiyonumuz gelen sayıları yazıya çevirip harflerini sayıyor.
    def harfTopla(sayi):
        basamak = 1
        toplamHarf = 0
        for i in sayi[::-1]:
            sayiYazi = basamaklar[basamak][int(i)].replace(" ","")
            toplamHarf += len(sayiYazi)
            basamak += 1
        return toplamHarf
# Burada döngü ile 1 den girilen sayıya kadar olan sayıları string yapıp 
# harfTopla fonksiyonuna gönderiyoruz
    for j in range (1,sayi+1):
        toplam += harfTopla(str(j))
    print(f"1 den {sayi} sayısına kadar olan sayılar harflerinin toplamı : {toplam}")
sayiHarfSayar(1000)