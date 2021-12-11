c = []

for i in range(1, 1000000):
    for digit in str(int(i)):
        c.append(int(digit))

result = 1
for i in range(7):
    print(10**i -1)
    result *= c[10**i -1]

print(result)
