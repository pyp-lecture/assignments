#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Aufgabe 1:
def cats(count):
    if count < 4:
        return "Die Anzahl der Katzen: " + str(count)
    else:
        return "Viel zu viele Katzen."

# Aufgabe 2:
def donauschiff():
    c=str("Donaudampfschiffahrtsgesellschaftsstewardess") 
    liste=list(c)
    Deduplicate = list(set(liste)) 
    Länge=len(liste)
    Länge2=len(Deduplicate)
    return liste , Länge , Deduplicate, Länge2

# Aufgabe 3:
def char_counter():
    lang = 0
    anzahla = 0
    Liste = [
        "cat", "dog", "crocodile", "bird", "elephant", "giraffe", "stork",
        "worm", "warthog", "kiwi", "kangaroo", "snake", "monkey"
    ]
    for i in Liste[:]:
        if len(i) >= 5:
            lang = lang + 1
    Liste.sort(reverse=True)
    for i in Liste[:]:
        anzahla = anzahla + i.count("a") + i.count("A")
    return len(Liste), lang, Liste, anzahla

# Aufgabe 4:
"""
Aufgabe 4: Tuple sortieren

Erstellen Sie diese Liste: [(1, 9), (3, 2), (31, 3, 1), (4, 33)] 
und sortieren Sie die Liste aufsteigend nach dem 
jeweils letzten Element des Tuples. 

def add(a,b):
    return a+b

add2 = lambda a,b: a+b

"""
def tuple_sorter():
    zahlenliste = [(1, 9), (3, 2), (31, 3, 1), (4, 33)]
    zahlenliste.sort(key=lambda x: x[-1])
    print(zahlenliste)

# Aufgabe 5:
"""
Aufgabe 5: Oh, wie schön ist List Comprehension!

Schreiben Sie eine Funktion, die für den Input einer Liste von Zahlen
eine Liste identischer Länge und die verdoppelten Zahlen des Inputs zurückgibt.
Beispiel: Input: [1, 2, 3, 4, 5]) 
Output: [2, 4, 6, 8, 10]

"""
def doubleit(eingabe):
    ausgabeliste = []
    for i in eingabe:
        ausgabeliste.append(i*2)
    return ausgabeliste

def list_comprehension(eingabe):
    ausgabeliste = [i*2 for i in eingabe if i> 2]
    return(ausgabeliste)

# Aufgabe 6:
def tuple_addition(eingabetuple):
    """tt = (23, 524, 668, 4, 26, 893, 86) 
    Ermitteln Sie den höchsten Wert im Tuple tt und 
    addieren Sie diesen zum Wert, der den Index 2 im Tuple belegt. 
    Die Funktion soll das Ergebnis zurückgeben."""
    #print(max(eingabetuple))
    """ 
    Wir haben noch ausprobiert:
    Wie ist das denn mit anderen Objekten z.B. Listen?
    das max Element zwischen verschiedenen Listen findet man heraus in dem man 
    >>> from itertools import chain
    >>> max(chain(liste1, liste2))

    """

    #print(eingabetuple[2])
    return max(eingabetuple) + eingabetuple[2]



if __name__ == "__main__":
    print("Aufgabe 1:")
    acht_katzen = cats(8)
    print(acht_katzen)
    zwei_katzen = cats(2)
    print(zwei_katzen)
    
    print("Aufgabe 2:")
    wort_liste , wort_länge , Deduplicate_liste, wort_länge_deduplicate = donauschiff()
    print(wort_länge)
    print(wort_länge_deduplicate)

    print("Aufgabe 3:")
    länge_tierliste, tier_länger_5, sortierte_liste, anzahla = char_counter()
    print("1. Wie viele Tiere sind in Ihrer Liste, die mit 5 und mehr Buchstaben geschrieben werden?",tier_länger_5)
    print("2. Sortieren Sie die Tierliste alphabetisch - von Z nach A.",sortierte_liste)
    print("3. Wie oft taucht der Buchstabe a/A in Ihrer Tierliste auf?", anzahla)

    print("Aufgabe 4:")
    tuple_sorter()

    print("Aufgabe 5:")
    eingabeliste = [1,2,3,4,5]
    doppelliste = doubleit(eingabeliste)
    print(doppelliste)
    print("List comprehension")
    neueliste = list_comprehension(eingabeliste)
    print(neueliste)


    print("Aufgabe 6:")
    eingabetuple = (23, 524, 668, 4, 26, 893, 86) 
    added_numbers = tuple_addition(eingabetuple)
    print(added_numbers)