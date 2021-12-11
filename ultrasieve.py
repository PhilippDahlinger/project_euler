# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:19:15 2019

@author: phili
"""
import math
import pickle
from tqdm import tqdm

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

        

if __name__ == "__main__":
    primes = sieve(1000000)
    pickle.dump(primes, open("primes.p", "wb") )
    print("done")
