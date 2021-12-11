# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:11:26 2019

@author: phili
"""

from tqdm import tqdm


def is_abundant(n):
    result = 0
    for i in range(1,n):
        if n%i == 0:
            result += i
    return result > n



a_list = []
x = 28124
for i in tqdm(range(1, x)):
    if is_abundant(i):
        a_list.append(i)

result= {}
for i in range(1, x):
    result[i] = True
for i in tqdm(a_list):
    for j in a_list:
        if j < i: 
            continue
        try:
            result[i+j] = False
        except:
            pass

sumi = sum([a for a in result.keys() if result[a]])
print(sumi)
        
