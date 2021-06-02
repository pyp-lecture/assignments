#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Aufgabe 1:

def de_en(dictionary, wort):
    uebersetzug = ("Wort nicht gefunden!", "")
    found = False

    for key, value in dictionary.items():
        if(wort == key):
            uebersetzug = value, "de_en"
            found = True

    if(found == False):
        for key, value in dictionary.items():
            if(wort == value):
                uebersetzug = key, "en_de"

    return uebersetzug

from googletrans import Translator
def smart_translators():
    translator = Translator 
    text = input("Welcher Text soll übersetzt werden")
    Sprache = input("in welche sprache?")
    Ergebnis = translator.translate(text, Sprache).text
    return Ergebnis

# Aufgabe 2:
# 1. Wie viele Buchstaben enthält der Text insgesamt?
# 2. Betrachten Sie jede Hälfte des Satzes. Welcher Teil enthält mehr Vokale?
# # 1.
def count_chars(dic):
    buch=0
    for i in dic:
        buch=buch+len(dic[i])
    return buch

# 2.
def vokale(ein):
    vok=0
    for i in ein:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        # oder kürzer?
            vok=vok+1
    return vok

def half_vokale(dic):
    anz=0
    anz2=0

    for i in dic:
        if i<=len(dic)/2:
            anz=anz+vokale(dic[i])
        
        else:
            anz2=anz2+vokale(dic[i])

    return anz, anz2



# Aufgabe 3:
import math

# 1.
def stringhalbierer(wort):
    a=math.ceil(len(wort)/2)

    return print(wort[:a],wort[a:])


# 2.
def zusammen(eina,einb):
    a=math.ceil(len(eina)/2)
    b=math.ceil(len(einb)/2)

    return print(eina[:a]+einb[:b]+eina[a:]+einb[b:])

def halbhalb(arg1, arg2=None):
    if len(arg1) % 2:
        split = 1 + int(len(arg1) / 2)
    else:
        split = int(len(arg1) / 2)
    str1 = arg1[:split]
    str2 = arg1[split:]
    if not arg2 == None:
        if len(arg2) % 2:
            split = 1 + int(len(arg2) / 2)
        else:
            split = int(len(arg2) / 2)
        str1 = str1 + arg2[:split]
        str2 = str2 + arg2[split:]

    return str1, str2

# Aufgabe 4:
def verbinden(d1, d2):
    summe = {**d1, **d2}
    return summe

def aus_2_mach_1(d1, d2):
    for key in dict2.keys():
        dict1[key] = dict2[key]
    print(dict1)
    

# Aufgabe 5:

def changePay(name, newSalary):
    for n, s in payDict.items():
        for key in s:
            if name == s[key]:
                payDict[n].update({'salary':newSalary})
    return payDict

def zweiterTeil():
    summe = 0
    for n, s in payDict.items():
        for key in s:
            if 'Steph' == s[key] or 'Melanie' == s[key] or 'David' == s[key] or 'Astrid' == s[key]:
                old = payDict[n]['salary']
                payDict[n].update({'salary': old + 500})
        #print(payDict[n]['salary'])
        summe += int(payDict[n]['salary'])
    return (summe/len(payDict))

# Aufgabe 6:

def loeschen(set1, set2):
    set3 = set1 & set2
    return(set3)

# Aufgabe 7:
def HelloAgain(wort):
    ausgabe = ''
    for i in wort:
        if i not in ausgabe:
            ausgabe += i
        else:
            ausgabe=ausgabe+'*'
    return ausgabe


if __name__ == "__main__":
    # Aufgabe 1:
    print("Aufgabe 1:")
    # Zuerst bestücken wir 
    d = {}
    d['Antriebsritzel'] = 'drive pinion'
    d['Biegeeigenschaft'] = 'bending property'
    d['Drehklappe'] = 'butterfly valve'
    d['Istspiel'] = 'actual clearance'
    d['Keilriemen'] = 'V-belt'

    wort = "Keilriemen"
    print(f"{wort} <-> {de_en(d, wort)}")

    wort = "butterfly valve"
    print(f"{wort} <-> {de_en(d, wort)}")

# Aufgabe 2:
    print("Aufgabe 2:")
    dic={1:"Gallia", 2:"est", 3:"omnis", 4:"divisa", 5:"in", 6:"partes", 7:"tres", 8:"quarum", 9:"unam", 10:"incolunt", 11:"Belgae", 12:"aliam", 13:"Aquitani", 14:"tertiam", 15:"qui", 16:"ipsorum", 17:"lingua", 18:"Celtae", 19:"nostra", 20:"Galli", 21:"appellantur"}
    anzahl_zeichen = count_chars(dic)
    print("Gesamtanzahl der Buchstaben:",anzahl_zeichen)

    anz, anz2 = half_vokale(dic)
    print("Vokale in der ersten Satzhälfte:",anz,"\n","Vokale in der zweiten Satzhälfte:",anz2)


# Aufgabe 3:
    print("Aufgabe 3:")
    stringhalbierer('abcde')
    zusammen('abcd','xy')
    print(halbhalb('abcde'))
    print(halbhalb('abcd', 'xy'))



# Aufgabe 4:
    print("Aufgabe 4:")
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    verbindung = verbinden(dict1, dict2)
    print(verbindung, '\n')
    verbindung2 = aus_2_mach_1(dict1, dict2)
    print(verbindung2, "\n")
    # das ginge auch:
    """
    dict1.update(dict2)
    print(dict1)

    """
    
# Aufgabe 5:
    print("Aufgabe 5:")
    payDict = { 'emp1': {'name': 'Karen', 'salary': 7500},
            'emp2': {'name': 'Steph', 'salary': 8000},
            'emp3': {'name': 'Cynthia', 'salary': 6500},
            'emp4': {'name': 'Paul', 'salary': 4500},
            'emp5': {'name': 'Myriam', 'salary': 180000},
            'emp6': {'name': 'Steven', 'salary': 2500},
            'emp7': {'name': 'Astrid', 'salary': 6500},
            'emp8': {'name': 'David', 'salary': 1000},
            'emp9': {'name': 'Melanie', 'salary': 2340}
    } 
    #changePay(input('Geben Sie den Namen ein:\n'),input('Geben Sie den neuen Gehalt ein:\n'))
    print("Das ist das neue Gehaltsbuch.", payDict)
    print('Der Durschnitt der neune Gehaelter betraegt: ', zweiterTeil() )
# Aufgabe 6:
    print("Aufgabe 6:")
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    neu_set1 = loeschen(set1, set2)
    print(neu_set1)

# Aufgabe 7:
    print("Aufgabe 7:")
    neues_Schiff = HelloAgain('Donaudampfschiffahrtsgesellschaftskapitän')
    print(neues_Schiff)