#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:36:18 2023

@author: gw
"""

n =list(input())
b=n.copy()
#print(n)
cnt=0

while True:
    if len(n) < 2:
        n.insert(0,'0')
        a=n
        #print(a)
    else:    
        a=n
    '''
    c=list(str(int(a[0])+int(a[1])))
    print(c)
    n=list(str(int(a[-1])*10+int(c[-1])))
    cnt+=1
    '''
    #break
    c =sum(list(map(int,a)))
    c =list(str(c))
    n=list(str(int(a[-1])*10+int(c[-1])))
    #print(n)
    cnt+=1
    
    if ''.join(b) ==''.join(n):
    #b[0] == n[0] and b[1]==n[1]:
        break
print(cnt)