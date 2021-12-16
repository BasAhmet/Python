stringNum = [[""],
["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz","on"],# Birler
["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan",],# Onlar
["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"],# Yüzler
["bin","bir bin","iki bin","üç bin","dört bin","beş bin","altı bin","yedi bin","sekiz bin","dokuz bin"],# Binler
["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"],# On Binler
["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"]]# Yüz Binler
while True:
    number = input("Yazıya çevrilecek sayı (Çıkış için 'q') : ")
    if number == "q":
        break
    strNumber = str(number)
    if len(strNumber) > 6:
        print(f"Şimdilik en fazla {len(stringNum)-1} basamak uzunluğunda sayı giriniz.")
        continue
    yaziylaSayi = ""
    for i in range(len(strNumber)):
        basamak = len(strNumber)-i
        basamakNumber = int(strNumber[i])
        if len(strNumber) == 4 and basamakNumber == 1:
            numberToString = stringNum[basamak][basamakNumber-1]
        else:
            numberToString = stringNum[basamak][basamakNumber]
        yaziylaSayi = yaziylaSayi + numberToString + " "
    print(yaziylaSayi)