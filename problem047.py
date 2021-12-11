import helper
from tqdm import tqdm

size = 1000000
primes = helper.sieve(size)
factor_dict = {}

def factor_sieve(n):
    factors = [[] for i in range(n)]
    for pointer in tqdm(range(2, n)):
        if len(factors[pointer]) == 0:
            # new prime
            for j in range(pointer, n, pointer):
                factors[j].append(pointer)
    return factors


def prime_factors(n):
    assert n != 0
    prime_pointer = 0
    new_factor = None
    while n != 1:
        try:
            rest_factors = factor_dict[n]
            if new_factor is None:
                return rest_factors
            else:
                rest_factors.append(new_factor)
            return rest_factors
        except KeyError:
            p = primes[prime_pointer]
            if n % p == 0:
                n = n // p
                new_factor = p
            else:
                prime_pointer += 1
    if new_factor is None:
        return []
    else:
        return [new_factor]


factors = factor_sieve(size)
    

i = 1
lowest = None
while i < size:

    hit = True
    for j in range(4):
        if len(factors[i+j]) != 4:
            hit = False
            break
    if hit:
        lowest = i
        print(i)
        print(factors[i])
        break
    i += j + 1

if lowest is not None:
    print(i, factors[i])
    print(i+1, factors[i+1])
    print(i+2, factors[i+2])
    print(i+3, factors[i+3])