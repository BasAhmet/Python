sayi = 1000
exit = True
for i in range(1,sayi):
    for j in range(i+1,sayi):
        for k in range(j+1,sayi):
            if i != j != k:
                if 1000 % (i+j+k)==0:
                    if i**2+j**2==k**2:
                        kat = int(1000/(i+j+k))
                        sayilar = [i*kat,j*kat,k*kat]
                        print(f"a = {sayilar[0]}\nb = {sayilar[1]}\nc = {sayilar[2]}")
                        exit = False
                        break
    if exit == False:
        break