kareToplam = 0
toplamKare = 0
for i in range(1,101):
    kareToplam += i**2
    toplamKare += i
fark = (toplamKare**2) - kareToplam
print(fark)