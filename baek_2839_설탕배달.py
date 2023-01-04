# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:08:03 2023

@author: 기원
"""

N = int(input())
five_max = N//5
i = 0
cnt = 0
while True:
    five = five_max - i
    b = N - (five*5)
    if five<0:
        print(-1)
        break
    
    if b % 3 == 0:
        three = b//3
        cnt = five + three
        print(cnt)
        break
    elif b%3 != 0:
        i+=1
        
    