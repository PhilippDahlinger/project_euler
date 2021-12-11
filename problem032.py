import pickle
from tqdm import tqdm
import functools

perms = pickle.load(open("perms.p", "rb"))

products = []
for perm in tqdm(perms):
    # 2 3 4
    a = 10*perm[0] + perm[1]
    b = 100*perm[2] + 10 * perm[3] + perm[4]
    c = 1000*perm[5] + 100 * perm[6] + 10*perm[7] + perm[8]
    if a*b ==c:
        products.append(c)
    # 4 1 4
    a = 1000*perm[0] + 100*perm[1] + 10*perm[2] + perm[3]
    b = perm[4]
    c = 1000*perm[5] + 100 * perm[6] + 10*perm[7] + perm[8]
    if a*b == c:
        products.append(c)

print(products)
prods = list(set(products))
print(sum(prods))
