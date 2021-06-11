#!/usr/bin/env python
 #-*- coding: utf-8 -*-

import random

zahl = random.randrange(1,100)
tipp = 0
versuche = 0
while tipp != zahl:
    versuche = versuche + 1
    print("Bitte Tipp eingeben")
    tipp = int(input())
    if tipp > zahl:
        print("Der Tipp war zu hoch")
    elif tipp < zahl: 
        print("Der Tipp war zu niedrig")
    else:
        break
print ("Richtig! Es wurden",versuche,"Versuche benötigt.")