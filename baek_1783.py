#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:23:15 2023

@author: gw
"""
n,m = map(int,input().split())
if n == 1:
    print(1)
    
elif n == 2:
    print(min(4,(m+1)//2))
    
else:
    if m <= 6:
        print(min(4,m))
    else:
        print(m-2)