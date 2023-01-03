# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:47:12 2023

@author: 기원
"""

money = int(input())

cnt = 0

five_max = money // 5
i=0
while True:
    five = five_max-i
    #print(five)
    a = money-(five*5)
    #print(a)
    if five<0:
        print(-1)
        break
    
    if a%2==0:
        two = a//2
        cnt = five+two
        print(cnt)
        break
    elif a%2 != 0:
        i+=1
        
      


'''
5로나누고 2로나누고
5하나 줄이고 2로나누고
'''
    