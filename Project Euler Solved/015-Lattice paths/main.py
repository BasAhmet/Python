# Bu Problem Kombinasyon Yardımıyla Çözülebilir.
from math import factorial
dikey = 20
yatay = 20
from math import factorial
rota = factorial(dikey+yatay)/(factorial(dikey)*factorial(yatay))
print(f"{yatay} x {dikey} olan bir ızgarada sol üstten sağ alta {int(rota)} tane yol vardır.")