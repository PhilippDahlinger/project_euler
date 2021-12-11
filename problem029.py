result = []
for a in range(2, 101):
    for b in range(2,101):
        result.append(a**b)
result = set(result)
print(len(result))