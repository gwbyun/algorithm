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
    
'''
123123
앞에서 하나씩 비교하면서 지워나감
작은거 발견하면 넘어가서 스택에 저장
제거 횟수 종료시 출력

'''    
    
    
    
    
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
