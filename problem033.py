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

def test_equal(num1, denom1, num2, denom2):
    gcd1 = gcd(num1, denom1)
    gcd2 = gcd(num2, denom2)
    short_num1 = num1//gcd1
    short_denom1 = denom1//gcd1
    short_num2 = num2//gcd2
    short_denom2 = denom2//gcd2
    return short_num1 == short_num2 and short_denom1 == short_denom2

result = []

for equal in range(1, 10):
    for a in range(1, 10):
        for b in range(1, 10):
            num1 = a*10 + equal
            denom1 = equal * 10 + b
            if num1 == denom1:
                continue
            num2 = a
            denom2 = b
            if num1 > denom1:
                num1, denom1 = denom1, num1
                num2, denom2 = denom2, num2
            if test_equal(num1, denom1, num2, denom2):
                result.append((num1, denom1))

answer_num = 1
answer_denom = 1
for frac in result:
    answer_num *= frac[0]
    answer_denom *= frac[1]

print(answer_num, answer_denom)
g = gcd(answer_num, answer_denom)
print(answer_num//g, answer_denom//g)
