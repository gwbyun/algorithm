# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:29:15 2022

@author: user
"""
n = int(input())
graph =[list(map(int, input())) for _ in range(n)]

num = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if x<0 or x>=n or y <0 or y>=n:
        #시작점이 범위 밖일경우 종료
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
            
        return True
    #모두 0이거나 범위 밖일경우 False반환
    return False

count = 0
# 단지내 건물수
result = 0
# 단지수

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(count)
            result +=1
            count = 0
            
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])