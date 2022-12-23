#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:08:41 2022

@author: gw
"""
from collections import deque

n, m = int(input.split())
graph =list()
for _ in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # deque
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >= n or ny<0 or ny>=m:
                continue
            #if next state is outside
            if graph[nx][ny] == 0:
                continue
            #if next state is wall
            
            if graph[nx][ny]== 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))
                