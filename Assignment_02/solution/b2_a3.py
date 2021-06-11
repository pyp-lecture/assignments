#!/usr/bin/env python
 #-*- coding: utf-8 -*-

from math import sqrt

N = 1000
gestrichen=[True,True]
prim=[]
for i in range(2,N):
    gestrichen.append(False)

for i in range(0,int(sqrt(N))):
    if not gestrichen[i]:  #Hinzufügen der Primzahl
        prim.append(i)
        for j in range(i,(N//i)): #Streichen der Vielfachen
            if i*j <= N:
                gestrichen[i*j] = True

for i in range(int(sqrt(N)), N-1):
    if not gestrichen[i]:
        prim.append(i)

for i in range(0,len(prim)):
    print(prim[i])
