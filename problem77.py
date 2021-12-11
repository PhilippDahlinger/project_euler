# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:19:15 2019

@author: phili
"""
import math

def sieve(n):
    n = n+1
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    for i in range(4, n, 2):
        primes[i] = False
    
    for i in range(3,math.floor(math.sqrt(n))+1, 2):
        if not primes[i]: continue
        primes[i*i::2*i] = [False]*((n - i*i - 1)//(2*i) + 1)
   
    
    return primes

N = 10000
        
sieb = sieve(N)
primes = [i for i in range(N) if sieb[i]]
primes = list(enumerate(primes))

pkn = [0]*N
for n in range(2,N):
    pkn[n] = pkn[n-1]
    if sieb[n]:
        pkn[n] += 1

print(pkn)
moegl = [ [0]*pkn[n] for n in range(N)]
minimum = 5000

for n in range(2,N):
    for k, p in primes[pkn[n]-1::-1]:
        if k + 1 < len(primes):
            _, biggerP = primes[k+1]
            if n >= biggerP:
                moegl[n][k] = moegl[n][k+1]
        if p <= n-p:
            moegl[n][k] += moegl[n-p][k]
        elif n-p == 0:
            moegl[n][k] += 1
#        if moegl[n][0] >= minimum:
#            print(n)
#            break
#    else:
#        continue
#    break

print(moegl[-1])
