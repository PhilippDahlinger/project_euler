import numpy as np
import ultrasieve




primes = np.array(ultrasieve.sieve(1000000))



def check_length(l):
    cur = np.sum(primes[0:l])
    # if cur > primes[-1]:
    #     return False
    if cur in primes:
        print(cur)
    for i in range(len(primes) - l):
        cur -= primes[i]
        cur += primes[i+l]
        if cur > primes[-1]:
            return
        if cur in primes:
            print(f"length: {l}, prime: {cur}")


for l in range(21, 547):
    check_length(l)
