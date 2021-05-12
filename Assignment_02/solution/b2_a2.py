#!/usr/bin/env python
 #-*- coding: utf-8 -*-

def average(a) :
    summe = sum(a)
    anzahl = len(a)
    mittelwert = summe/anzahl
    return mittelwert


if __name__ == "__main__":
    a = [2, 8, 9, 2, 7, 20]
    print("Der Mittelwert beträgt : ", average(a))