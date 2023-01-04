#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:44:11 2022

@author: gw
"""

from collections import deque

n = int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

print(graph)
for i in range  (1,n+1):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1
    
def bfs(V):
    count = 0
    visited[V] = 1
    
    queue = deque(graph[V])
    
    while queue:
        V=queue.popleft()
        for i in range  (1,n+1):
            if visited[i]==0 and graph[V][i] == 1:
                queue.append(i)
                visited[i]=1
                count =+1
                
    return count

print(bfs(1))