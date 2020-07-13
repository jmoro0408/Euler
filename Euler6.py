#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:43:29 2020

@author: James
"""
#This is a solution to Project Euler Problem 6

x = [i**2 for i in range(1,101)]
sumx = sum(x)

y = range(1,101)
sumy = sum(y)
sumy2 = sumy**2

diff = sumy2 - sumx
print(diff)