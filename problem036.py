result = []
for i in range(1000000):
    integer = str(i)
    binary = f"{i:b}"
    if integer == integer[::-1] and binary == binary[::-1]:
        result.append(i)

print(result)
print(sum(result))


