# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:43:02 2020

@author: JM070903
"""

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers
"""


def palindrome(x,y):
    total = x* y
    if str(total) == str(total)[::-1]:
        print(total)
    return 
        
for i in range (100,999):
    for j in range (100,999):
        palindrome(i,j)



            
            