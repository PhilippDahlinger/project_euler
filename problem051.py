from helper import sieve
from tqdm import tqdm
import pickle


primes = pickle.load(open("data/primes_e6.p", "rb"))

primes = [str(p) for p in primes]

num_same_digits = 2

for p in tqdm(primes):
    finished = False
    for digit in [0, 1, 2]:
        if p.count(str(digit)) >= num_same_digits:
            num_primes = 1
            for other_digit in range(digit + 1, 10):
                replaced_p = p.replace(str(digit), str(other_digit))
                if replaced_p in primes:
                    num_primes += 1
            if num_primes >= 8:
                print(p)
                finished = True
                break
    if finished:
        break
