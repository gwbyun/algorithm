# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:48:15 2022

@author: user
"""
#도시의 개수
N = int(input())
#도시간 거리

dist = list(map(int,input().split()))
#graph =[list(map(int, input())) for _ in range(n)]
price = list(map(int,input().split()))

money=list()
count = 0
for i in range (N-1):
    count += dist[i]*min(price[:i+1])
    #print(i)
    #print((price[:i+1]))
print(count)