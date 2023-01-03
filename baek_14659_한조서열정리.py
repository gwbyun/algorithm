# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:13:59 2023

@author: 기원
"""

n = int(input())
h = list(map(int,input().split()))

cnt = 0
result = []
highest=0

'''
while True:
    #print(i)
        
    if h[highest]>=h[i]:
        cnt +=1
        #print(cnt)
    else:
        pivot = i
        if result < cnt:
            result = cnt
        cnt =0
    i+=1  
    if i == n:
        break
 '''   
    
for i in range (1,n):

    if h[highest]>=h[i]:
        cnt +=1
        #print(cnt)
    else:
        highest = i
        cnt =0    
    result.append(cnt)
        #print(cnt)
print(max(result))
#조건을 씨발 좆같이주네
