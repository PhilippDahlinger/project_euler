

def update(n):
    n_str = str(n)
    n_rev = "".join(reversed(n_str))
    return n + int(n_rev)


if __name__ == "__main__":
    non_lynchel = 0
    for n in range(1, 10000):
        for j in range(50):
            n = update(n)
            if n == int("".join(reversed(str(n)))):
                non_lynchel += 1
                break
    print(9999 - non_lynchel)
