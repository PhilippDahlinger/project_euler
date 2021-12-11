import ultrasieve
import bisect

def contains(l, x):
    i = bisect.bisect_left(l, x)
    return i != len(l) and l[i] == x


primes = ultrasieve.sieve(1000000)

result = []
for p in primes:
    if p < 10:
        continue
    p_s = str(p)
    hit = True
    # truncated test
    for i in range(1, len(p_s)):
        if not contains(primes, int(p_s[i:])):
            hit = False
            break
        if not contains(primes, int(p_s[:i])):
            hit = False
            break
    if hit:
        print(p)
        result.append(p)

print(result)
print(sum(result))
