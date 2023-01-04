# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 00:02:21 2022

@author: user
"""

n = int(input())
pivot = [500, 100, 50, 10, 5, 1]
x = (1000-n)
count = 0
for i in pivot:
    #print(i)
    count += x//i
    x = x%i
print(count)