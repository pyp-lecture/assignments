#!/usr/bin/env python
 #-*- coding: utf-8 -*-

def average(a) :
    mittelwert = sum(a)/len(a)
    return mittelwert


if __name__ == "__main__":
    a = (2, 8, 9, 2, 7, 20)
    print("Mittelwert : ", average(a))