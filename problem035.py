import ultrasieve
import bisect

def contains(l, x):
    i = bisect.bisect_left(l, x)
    return i != len(l) and l[i] == x


primes = ultrasieve.sieve(1000000)

result = []
for p in primes:
    p_s = str(p)
    hit = True
    for r in range(len(p_s)):
        p_s = p_s[1:] + p_s[0]
        if not contains(primes, int(p_s)):
            hit = False
            break
    if hit:
        print(p)
        result.append(p)

print(result)
print(len(result))
