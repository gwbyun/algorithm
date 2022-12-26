# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import deque
N = int(input())

graph = [list(map(int,input())) for _ in range(N)]

def bfs(graph,x,y):
    #상하좌우
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    #시작점 결정
    graph[x][y] = 0
    #탐색중인 위치 0으로 만들어 다시 방문하지 않도록
    cnt  = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            #시작점 상하좌우 이동
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >=N or ny < 0 or ny >= N:
                continue
            # 범위를 벗어나거나 0일경우 다시 탐색
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                #0으로 바꾼뒤 새로운 시작지점 등록
                cnt +=1
                
    return cnt
count = [bfs(graph,i,j) for i in range(N) for j in range(N) if graph[i][j]==1]

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])

