import numpy as np
squares = [i*i for i in range(1000)]

result = [0] * 1001
for a in range(1, 1000):
    for b in range(a, 1000):
        squared_c = a*a + b*b
        try:
            c = squares.index(squared_c)
            p = a+b+c
            if p <= 1000:
                result[a+b+c] += 1
        except ValueError:
            continue

print(np.argmax(result))
