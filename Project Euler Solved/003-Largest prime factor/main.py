number = 600851475143
num = number
import math
asalCarpanlar = []
for k in range(num):
    for i in range(3,num+1,2):
        asal = True
        ustSayi = int(math.sqrt(i))
        for j in range(2,ustSayi+1):
            if i % j == 0:
                asal = False
        if asal:
            if num % i == 0:
                num = int(num / i)
                asalCarpanlar.append(i)
                break
    if num == 1:
        break
enBuyukAsalBolen = max(asalCarpanlar)
print(f"{number} sayısının asal çarpanları : {asalCarpanlar}")
print(f"{number} sayısının en büyük asal çarpanı : {enBuyukAsalBolen}")