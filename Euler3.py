# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:59:57 2020

@author: JM070903
"""
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def pfactor(n):
    nn = int(math.sqrt(n))
    while n % 2 == 0:
        print(2)
        n = n / 2
    for i in range (3,nn):
        while n % i == 0:
            print(i)
            n = n / i
    if n > 2:
        print(n)
        
        
pfactor(600851475143)
    