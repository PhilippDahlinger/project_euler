import helper
from helper import contains
primes = helper.sieve(1000000)
double_squares = [2*i*i for i in range(1000)]
print(double_squares)

for i in range(1,1000000, 2):
    if contains(primes, i):
        continue
    # composite i
    for d_square in double_squares:
        if d_square > i:
            print(i)
            break
        diff = i - d_square
        if contains(primes, diff):
            break
