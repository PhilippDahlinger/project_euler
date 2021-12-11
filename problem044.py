from helper import contains
from tqdm import tqdm
import numpy as np

def pent_numbers(n):
    return [i*(3*i - 1)//2 for i in range(1,n+1)]

size = 20000
pents = pent_numbers(size)

for i in tqdm(range(size)):
    for j in range(i+1, size):
        if contains(pents, pents[j] - pents[i]) and contains(pents, pents[j] + pents[i]):
            print(pents[i] , pents[j])