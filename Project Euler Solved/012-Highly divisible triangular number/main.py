bolenSayisi = 500
ucgenSayi= 0
bolenler = []
i = 1
while True:
    ucgenSayi += i
    for j in range(1,int(i/2)+1):
        if i % j == 0:
            bolenler.append(j)
    bolenler.append(i)
    print(f"{ucgenSayi} üçgen sayısının bölenleri {len(bolenler)} tane : {bolenler}")
    if len(bolenler) > bolenSayisi :
        break
    i += 1
    bolenler = []