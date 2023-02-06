#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:35:49 2023

@author: gw
"""
import sys
a = list(input().split('.'))
poly_1 = 'AAAA'
poly_2 = 'BB'
#print(a)
graph=list()

for i in range (len(a)):
    '''
    print()
    print(a[i])
    print(len(a[i]))
    '''
    #if len(a[i]) == 0:
        #graph.append('.')
    if len(a[i])%2 != 0:
        
        print(-1)
        sys.exit()
    
for i in range (len(a)):    
    if (len(a[i])//2)%2 ==0:
        n=len(a[i])/4
        #print( poly_1 * int(n))
        a[i] = poly_1 * int(n)
        graph.append(poly_1 * int(n))
        
        #print(a)
    elif (len(a[i])//2)%2 !=0:
        poly_1_num=len(a[i])//4
        poly_2_num=(len(a[i])%4)//2
        graph.append(poly_1*poly_1_num+poly_2*poly_2_num)
        
print('.'.join(graph))