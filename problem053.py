from scipy.special import comb

if __name__ == "__main__":
    count = 0
    for n in range(1, 101):
        for k in range(1, n):
            binom = comb(n, k, exact=True)
            if binom > 1000000:
                count += 1

    print(count)