from helper import sieve
import pickle

for e in range(5, 11):
    primes = sieve(int(10**e), use_tqdm=True)
    pickle.dump(primes, open(f"data/primes_e{e}.p", "wb"))
    print(f"saved primes up to 10 ** {e}")