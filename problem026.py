import numpy as np

def division(a,b):
    result = []
    for i in range(10000):
        a *= 10
        x = a // b
        result.append(x)
        a -= b*x
    result = result[::-1]
    return result

def get_cycle_length(l):
    cycle = [l[0]]
    while True:
        found_cycle = True
        for i in range(2000):
            if l[i] != cycle[i%len(cycle)]:
                cycle.append(l[len(cycle)])
                found_cycle = False
                break
        if found_cycle:
            return len(cycle)

            

clens = []
for b in range(1,1001):
    clens.append(get_cycle_length(division(1,b)))

m = max(clens)
print(m)
print(clens.index(m))

