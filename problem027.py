import pickle
from tqdm import tqdm

primes = pickle.load(open("primes.p", "rb"))

def test_formula(formula):
    n = 0
    counter = 0
    while True:
        x = formula(n)
        if x < 0:
            break
        if x in primes:
            counter += 1
            n += 1
        else:
            break
    return counter


max_counter = 0
result = None
for b in tqdm(range(0, 1001)):
    if b not in primes:
        continue
    for a in range(-999, 1000):
        if a % 2 == 0 and b != 2:
            continue
        formula = lambda n: n*n + a*n + b
        c = test_formula(formula)
        
        if c > max_counter:
            max_counter = c
            result = (a,b)
        
print(result)
print(max_counter)
print(result[0]*result[1])


