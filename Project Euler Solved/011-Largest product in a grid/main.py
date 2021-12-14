numbers = []
buyukSayi = 0
with open("problem11.txt","r",encoding="utf-8") as file:
    for i in file:
        satir = i.split()
        numbers.append(satir)
for j in range(len(numbers)):
    for k in range(len(numbers)-3):
        carpimYatay = int(numbers[j][k])*int(numbers[j][k+1])*int(numbers[j][k+2])*int(numbers[j][k+3])
        carpimDikey = int(numbers[k][j])*int(numbers[k+1][j])*int(numbers[k+2][j])*int(numbers[k+3][j])
        if j < 17:
            carpimSagAlt = int(numbers[j][k])*int(numbers[j+1][k+1])*int(numbers[j+2][k+2])*int(numbers[j+3][k+3])
            carpimSagYukari = int(numbers[j+3][k])*int(numbers[j+2][k+1])*int(numbers[j+1][k+2])*int(numbers[j][k+3])
        if carpimYatay > buyukSayi:
            buyukSayi = carpimYatay
            yon = "Yatay"
            a = j+1
            b = k+1
        if carpimDikey > buyukSayi:
            buyukSayi = carpimDikey
            yon = "Dikey"
            a = k+1
            b = j+1
        if carpimSagAlt > buyukSayi:
            buyukSayi = carpimSagAlt
            yon = "Sağ Alt"
            a = j+1
            b = k+1
        if carpimSagYukari > buyukSayi:
            buyukSayi = carpimSagYukari
            yon = "Sağ Yukarı"
            a = j+3+1
            b = k+1
print(f"Başlangıcı ({a},{b}) koordinatlarında.")
print(f"{yon} yönünde.")
print(buyukSayi)