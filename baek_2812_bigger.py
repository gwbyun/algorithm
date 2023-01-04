#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:29:51 2023

@author: gw
"""

n,k = map(int,input().split())
numbers = input()

stack = []

for number in numbers:
    while stack and stack[-1] < number and k > 0:
        print(stack)
        stack.pop()
        k -= 1
    stack.append(number)
    
    
    
    
    
    
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
