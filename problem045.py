size = 30000000
T = [n*(n+1)//2 for n in range(size)]
P = [n*(3*n-1)//2 for n in range(size)]
H = [n*(2*n-1) for n in range(size)]

p1, p2, p3 = 2, 2, 2

result = []

while p1 < size:
    if T[p1] == P[p2]:
        if T[p1] > H[p3]:
            p3 += 1
            continue
        if T[p1] < H[p3]:
            p1 += 1
            continue
        if T[p1] == H[p3]:
            print(T[p1])
            result.append(T[p1])
            p1 += 1
            continue
    if T[p1] > P[p2]:
        p2 += 1
        continue
    if  T[p1] < P[p2]:
        p1 += 1
        continue

print(result)