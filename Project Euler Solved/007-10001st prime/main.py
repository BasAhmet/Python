import math
asallar = [2]
i = 3
while len(asallar)<10002:
    asal = True
    ustSayi = int(math.sqrt(i))
    for j in range(2,ustSayi+1):
        if i % j == 0:
            asal = False
    if asal:
        asallar.append(i)
    i += 2
print("10001. asal : ",asallar[10000])