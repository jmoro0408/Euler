#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:09:59 2020

@author: James

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
1 to 20?
"""

#check in number is divisiable

import time

t0 = time.time()

def ifDividesAll(num):
  for i in range(2,21):
    if num % i != 0:
      return False
  return True

num = 20
while True:
  if ifDividesAll(num):
    break
  else:
    num = num + 1
print (num)

t1 = time.time()

total = t1-t0
print(total)