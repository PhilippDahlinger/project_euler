import numpy as np
import ultrasieve

primes = np.array(ultrasieve.sieve(10000))
primes = primes[primes > 1000]

for start in primes:
    for inc in range(2, 5000, 2):
        a = start
        b = start + inc
        c = b + inc
        if c >= 10000:
            break
        if b not in primes or c not in primes:
            continue
        digits_a = "".join(sorted(str(a)))
        digits_b = "".join(sorted(str(b)))
        digits_c = "".join(sorted(str(c)))
        if digits_a == digits_b and digits_a == digits_c:
            print(a,b,c)

