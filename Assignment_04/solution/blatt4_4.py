#!/usr/bin/env python
#-*- coding: utf-8 -*-

##  Aufgabe 4:
"""
Verbinden Sie die beiden dicitonaries zu einem.
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

"""
def verbinden(dict1, dict2):
    for key in dict2.keys():
        dict1[key] = dict2[key]
    return dict1

def verbinden_neues_dict(dict1, dict2):
    dict3 = dict1.copy()
    for key, value in dict2.items():
        dict3[key] = value
    return dict3

def verbinden_cool(dict1, dict2):
    summe = {**dict1, **dict2}
    return summe


# Aufgabe 5:
def changePay(name, new_salary):
    for id, info in payDict.items(): #info soll behandelt werden wie ein eigenes dictionary
        for key in info:
            if name == info[key]:
                payDict[id].update({'salary': new_salary})
    return payDict
# update der Gehälter:
def changePay_employees(salary_update):
    summe = 0
    for id, info in payDict.items():
        for key in info:
            if 'Steph'== info[key] or 'Melanie'== info[key] or 'David'== info[key] or 'Astrid'== info[key]:
                altes_Gehalt = payDict[id]['salary']
                payDict[id].update({'salary' : altes_Gehalt + salary_update})
        summe += payDict[id]['salary']
    return (summe/len(payDict))

# Aufgabe 6:
def sets_nicht_gemeinsam(set1, set2):
    set3 = set2 ^ set1
    set4 = set2 -  set1
    set5 = set1 - set2
    set6 = set1 & set2
    return set3

# Aufgabe 7:
def donauschiff(donau):
    out = ""
    for buchstabe in donau:
        if buchstabe not in out:
            out += buchstabe
        else: out = out + "*"
    return out

if __name__ == "__main__":
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    #print(verbinden(dict1, dict2))
    #print(verbinden_cool(dict1, dict2))
    #print(verbinden_neues_dict(dict1, dict2))
    #changePay(Karen, 8000)
    payDict = {
     'emp1': {'name': 'Karen', 'salary': 7500},
     'emp2': {'name': 'Steph', 'salary': 8000},
     'emp3': {'name': 'Cynthia', 'salary': 6500},
     'emp4': {'name': 'Paul', 'salary': 4500},
     'emp5': {'name': 'Myriam', 'salary': 180000},
     'emp6': {'name': 'Steven', 'salary': 2500},
     'emp7': {'name': 'Astrid', 'salary': 6500},
     'emp8': {'name': 'David', 'salary': 1000},
     'emp9': {'name': 'Melanie', 'salary': 2340}
    } 
    #print(payDict)
    #print(changePay("Karen", 8000))
    #print(changePay_employees(500))

    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    #print(sets_nicht_gemeinsam(set1, set2))

    donau= 'Donaudampfschiffahrtsgesellschaftskapitän'
    donauschiff(donau)
