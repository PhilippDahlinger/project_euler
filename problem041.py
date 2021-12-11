import ultrasieve

def pandigital(x):
    x_s = str(x)
    l = len(x_s)
    for i in range(1, l+1):
        if str(i) not in x_s:
            return False
    return  True

primes = ultrasieve.sieve(100000000, use_tqdm=True)
for p in primes[::-1]:
    if pandigital(p):
        print(p)
        break
