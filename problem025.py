# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:22:16 2019

@author: phili
"""

def fib():
    n = 1
    f1, f2 = 1,1
    while True:
        f1, f2 = f1+f2, f1
        n+= 1
        if len(str(f2)) >= 1000:
            return n
        
print(fib())