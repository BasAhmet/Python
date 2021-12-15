faktoriyel, sayi, toplam = 1, 100, 0
for i in range(1,sayi+1):
    faktoriyel *= i
for i in str(faktoriyel):
    toplam += int(i)
print(f"{sayi}! = {faktoriyel}\nsayısının rakamları toplamı : {toplam}")