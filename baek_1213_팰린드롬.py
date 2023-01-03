# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip()))
#word = list(map(str, input()))
word.sort() # 사전순으로 정렬하기 위해 오름차순 정렬
check = Counter(word)
print(check)

center=""
cnt = 0
for i in check:
    #print(i)
    if check[i] % 2 != 0:
       cnt+=1
       center += i
       word.remove(i)
       
    if cnt > 1:
          break
      
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    
    res = ""
    
    for i in range (0,len(word), 2):
        res += word[i]
        
    print(res + center + res[::-1])