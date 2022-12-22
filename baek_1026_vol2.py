#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:16:00 2022

@author: gw
"""

'''
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.
'''
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_pibot = sorted(a)
b_pibot = sorted(b, reverse=True)

#print(b)
#print(a)
count = 0
for x in range (n):
    count += a_pibot[x] * b_pibot[x]
print(count)
    