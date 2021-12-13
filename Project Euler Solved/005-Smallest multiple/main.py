sayi = 20
carpim = 1
for i in range(2,sayi+1): #
    asal = True           # # 
    for j in range(2,i):  # # # Burada asalları buluyoruz
        if i % j == 0:    # #
            asal = False  #
    if asal:              ##### Asal True gelirse sayi dan küçük kuvvetini çarpana ekliyoruz
        kuvvet = 1
        while True:
            carpan = i ** kuvvet
            if carpan > sayi:   ### Çarpan sayi yı geçtiğinde bir önceki kuvveti carpim ile çarpıyoruz
                carpan = i ** (kuvvet-1)
                carpim *= carpan
                break
            kuvvet += 1
print(carpim)