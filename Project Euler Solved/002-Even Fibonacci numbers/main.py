fibonacci = [1,2]
sum = 0
while True:
    lastNumber = fibonacci[-2]+fibonacci[-1]
    if lastNumber >= 4000000:
        break
    fibonacci.append(lastNumber)
for i in fibonacci:
    if i % 2 == 0:
        sum += i
print(fibonacci)
print(sum)