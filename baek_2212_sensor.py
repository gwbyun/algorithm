#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:04:41 2023

@author: gw
"""

n = int(input())
k = int(input())

sensor = list(map(int,input().split()))
sensor.sort()

array = []
for i in range(0,n-1):
    array.append(sensor[i+1] - sensor[i])
array.sort()

print(sum(array[:n-k]))