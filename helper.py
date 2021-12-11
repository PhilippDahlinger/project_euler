import bisect
import math
import pickle
from tqdm import tqdm


def contains(l, x, start=None, end=None):
    if start is None:
        i = bisect.bisect_left(l, x)
    else:
        assert end is not None
        i = bisect.bisect_left(l, x, lo=start, hi=end)
    return i != len(l) and l[i] == x


def permutations(symbols):
    if len(symbols) == 1:
        return [symbols]
    smaller = permutations(symbols[0:-1])
    s = symbols[-1]
    result = []
    for perm in smaller:
        for place in range(len(perm) + 1):
            new = perm.copy()
            new.insert(place, s)
            result.append(new)
    return result


def sieve(n, use_tqdm=False):
    if n % 2 == 0:
        n += 2
    else:
        n = n+1
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    for i in range(4, n, 2):
        primes[i] = False
    if use_tqdm:
        for i in tqdm(range(3,math.floor(math.sqrt(n))+1, 2)):
            if not primes[i]: continue
            primes[i*i::2*i] = [False]*((n - i*i)//(2*i) + 1)
    else:
        for i in range(3,math.floor(math.sqrt(n))+1, 2):
            if not primes[i]: continue
            primes[i*i::2*i] = [False]*((n - i*i)//(2*i) + 1)
    numbers = [i for i in range(n) if primes[i]]
    return numbers


def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        c = a % b
        a = b
        b = c
    if a < 0:
        return -a
    else:
        return a