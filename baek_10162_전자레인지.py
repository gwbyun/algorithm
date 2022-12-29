# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 21:53:47 2022

@author: user
"""

T = int(input())
time=[300, 60, 10]
count_a =[0, 0, 0]

for i in range (3):
    count_a[i] = T//time[i]
    T = T%time[i]
    
if T ==0:    
    print(count_a[0],count_a[1],count_a[2])
else :
    print(-1)