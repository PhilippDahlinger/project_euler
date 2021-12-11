# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:01:10 2019

@author: phili
"""
from tqdm import tqdm

def get_partner(n):
    result = 0
    for i in range(1,n):
        if n%i == 0:
            result += i
    return result



result = 0

for i in tqdm(range(1, 10000)):
    p = get_partner(i)
    if p > i and get_partner(p) == i:
        result += i
        result += p
print(result)
        
            