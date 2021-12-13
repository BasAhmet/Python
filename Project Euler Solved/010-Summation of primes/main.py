sayi=2000000
import math
asallarToplamı = 2
asallar = [2]
for i in range(3,sayi+1,2):
    asal = True
    ustSayi = int(math.sqrt(i))
    for j in range(2,ustSayi+1):
        if i % j == 0:
            asal = False
    if asal:
        asallar.append(i)
        asallarToplamı += i
        print(i)
print(asallar)
print(len(asallar),"tane",sayi,"sayısından daha küçük asal var.")
print("Toplamları : ",asallarToplamı)