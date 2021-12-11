from tqdm import tqdm
result = 0
for n in tqdm(range(10,10000000)):
    n_s = str(n)
    sumi = 0
    for l in n_s:
        sumi += int(l)**5
    if sumi == n:
        result += n
        print(n)
print(result)