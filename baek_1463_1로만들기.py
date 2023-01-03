# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:19:29 2023

@author: 기원
"""

x = int(input())

d = [0]*30001
#print(d)


for i in range(2, x+1):
    # 1을뺀다,
    d[i] = d[i-1]+1
    # x가 2로 나누어 떨어지면,2로 나눈다
    if i % 2 ==0:
        d[i] = min(d[i], d[i//2]+1)
    # x가 3으로 나누어떨어지면 3으로 나눈다
    if i % 3 ==0:
        d[i] = min(d[i], d[i//3]+1)
        
print(d[x])