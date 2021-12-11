import itertools

if __name__ == "__main__":
    gen = itertools.count(start=123)
    multiplier = [1,2,3,4,5,6]
    for n in gen:
        multiples = [n * multi for multi in multiplier]
        multiples = set(["".join(sorted(str(i))) for i in multiples])
        if len(multiples) == 1:
            print(n)
            break

