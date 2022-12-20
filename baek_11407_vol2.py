#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:14:06 2022

@author: gw
"""

'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오
'''
n,k = map(int, input().split())
print(n,k)
count = 0
graph = list()
for x in range(n):
    graph.append(int(input()))
#reversed is not change original graph

for x in reversed(graph):
    print(x)
    count += k//x
    k = k - x*(k//x)
print(count)