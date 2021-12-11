# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:10:17 2019

@author: phili
"""

def len_chain(n, knowledge):
    if n == 1:
        return 1
    if n in knowledge.keys():
        return knowledge[n]
    if n%2 == 0:
        result = len_chain(n//2, knowledge)+1
    else:
        result = len_chain(3*n +1, knowledge)+1
    knowledge[n] = result
    return result

knowledge = {}

maxi = 1
max_number = 1
for i in range(1, 1000000):
    result = len_chain(i, knowledge)
    if result > maxi:
        maxi = result
        max_number = i

print(max_number)