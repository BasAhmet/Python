zincirUzunlugu = 0
zincir = []
for i in range(999999,0,-1):
    print(i)
    zincir.append(i)
    a = i
    while True:
        if a % 2 == 0:
            a = int(a/2)
            zincir.append(a)
        elif a % 2 != 0:
            a = 3*a+1
            zincir.append(a)
        if a == 1:
            break
    if len(zincir)>zincirUzunlugu:
        zincirUzunlugu = len(zincir)
        baslangic = i
        zincirSon = zincir
    zincir = []
print(f"{baslangic} sayısı {zincirUzunlugu} zincir uzunluğuna sahip en uzun halkalı sayı.")
print(zincirSon)
#        837799         525