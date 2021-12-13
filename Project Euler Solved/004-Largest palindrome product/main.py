palindrom = 0
for i in range(100,1000):
    for j in range(100,1000):
        number = str(i * j)
        if number == number[::-1] and int(number) > int(palindrom):
            palindrom = number
            a = i
            b = j
print(f"Üç basamaklı iki sayının çarpımı ile oluşabilcek en büyük palindromik sayı :\n{a} x {b} = {palindrom}")