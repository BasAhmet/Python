sayilar = []
with open("problem13.txt","r",encoding="utf-8") as file:
    for sayi in file:
        sayilar.append(sayi)
toplam = 0
for i in range(len(sayilar)):
    toplam += int(sayilar[i])
strtoplam = str(toplam)
print("Sayıların toplamı : ",toplam)
print("İlk on basamak : ",strtoplam[-10:])