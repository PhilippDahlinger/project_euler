import math

factorials = {}
for i in range(10):
    factorials[i] = math.factorial(i)


def fact_sum(x):
    fact = 0
    number = 0
    length = len(x)
    for i, digit in enumerate(x):
        fact += factorials[digit]
        number += 10**(length - i-1)*digit
    return number == fact, number


result  = 0
for i in range(3, 1000000):
    x = str(i)
    x = list(x)
    x = [int(digit) for digit in x]
    res, number = fact_sum(x)
    if res:
        print(number)
        result += number

print(result)

