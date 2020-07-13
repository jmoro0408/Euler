#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:05:23 2020

@author: James
"""

#By considering the terms in the Fibonacci sequence whose values 
#do not exceed four million, find the sum of the even-valued terms.

from functools import lru_cache
@lru_cache(maxsize = 1000)

def fibonacci(n): #produce the fibonacci sequence for n terms
    if n <= 1:
       return n
    else:
        newfib = (fibonacci(n-1) + fibonacci(n-2))
        return newfib
        

for i in range (0,100): #find what value of n relates to a total of 4mil
    x = fibonacci(i)
    if x > 4000000:
        print("The term %s of the sequence produces a size no larger than 4mil" % str(i-1))
        break
    else:
        x = fibonacci(i)
    
total = 0  
for j in range(0,34): #iterate through fibonacci numbers less than 4 mil
  x = fibonacci(j)
  if x % 2 == 0: #if number is even, store it in variable "total"
    total = total + x
print("The sum of all even numbers in the fibonacci seqence less than 4mil is %s" % str(total))
