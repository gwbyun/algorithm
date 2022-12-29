# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:44:37 2022

@author: user
"""

n = int(input())
graph=list()
weight=list()
for _ in range (n):
    graph.append(int(input()))
#print(graph.sort())
graph.sort(reverse = True)

for i in range (n):
    weight.append(graph[i]*(i+1))

print(max(weight))