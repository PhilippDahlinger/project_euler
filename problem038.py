def pan_product(x, n):
    assert n > 1
    result = ""
    for i in range(1,n+1):
        result += str(x*i)
    return result

digits = [str(i) for i in range(1, 10)]

def check_pandigital(y):
    for i in digits:
        if i not in y:
            return False
    return True


result = []

for x in range(1, 10000):
    for n in range(2, 10):
        pan_prod = pan_product(x, n)
        if len(pan_prod) < 9:
            # check bigger n
            continue
        if len(pan_prod) == 9 and check_pandigital(pan_prod):
            result.append(int(pan_prod))
        if len(pan_prod) > 9:
            # next number
            break

print(result)
result.sort()
print(result[-1])

