triangle = []
with open("triangle.txt","r",encoding="utf-8") as file:
    for i in file:
        triangle.append(i.split())
        print(i,end="")
for j in range(len(triangle)-1):
    for i in range(len(triangle[-1])-1):
        triangle[-2][i] = max(int(triangle[-1][i]),int(triangle[-1][i+1])) + int(triangle[-2][i])
    triangle.pop()
print(f"\nEn büyük toplam : {triangle[0][0]}")