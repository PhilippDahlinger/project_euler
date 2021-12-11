# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:05:27 2019

@author: phili
"""

from collections import defaultdict
from functools import reduce

def gen_triangles():
    n = 1
    triangle = 0
    while True:
        triangle += n
        n += 1
        yield triangle
    

def pfz(n):
    if n <= 1:
        return defaultdict(lambda: 0)
    
    composition = defaultdict(lambda: 0)
    for d in range(2,n+1):
        if n%d == 0:
            composition = pfz(n//d)
            composition[d] += 1
            break
    return composition

n=1
old_pft = defaultdict(lambda: 0)
while True:
    comp = pfz(n+1)
    merge = defaultdict(lambda: 0)
    for key in old_pft:
        merge[key] += old_pft[key]
    for key in comp:
        merge[key] += comp[key]
    merge[2] -= 1
    for key in merge:
        merge[key] += 1
    result = reduce(lambda x,y: x*y, merge.values())
    if result >= 500:
        print(n, n*(n+1)//2, result)
        break
    n+= 1
    old_pft = comp
    