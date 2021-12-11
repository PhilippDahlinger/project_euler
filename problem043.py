import pickle

perms = pickle.load(open("perms.p", "rb"))
checks = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17}

result = []
for p in perms:
    if p[0] == 0:
        continue
    hit = True
    for k in checks.keys():
        if (p[k]*100 + p[k+1]*10 + p[k+2]) % checks[k] != 0:
            hit = False
            break
    if hit:
        p = [str(x) for x in p]
        n = int("".join(p))
        result.append(n)
        print(n)

print(sum(result))