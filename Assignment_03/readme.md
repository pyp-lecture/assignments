# Blatt 3: Listen und Tuple!

*Fällig: 18.05.2021*

Versuchen Sie nun, dieses Blatt zu lösen, indem Sie nur eine `.py`-Datei abgeben.
Rufen Sie in der Main-Methode alle Aufgaben nacheinander auf. Nutzen sie gerne die beiliegende `.py`-Datei und editieren Sie die Stellen, die mit `pass` markiert sind.

**Abgabe:** blatt_3.py
## Aufgabe 1: 4 cats are one cat too many
Schreiben Sie eine Funktion, die eine übergebene Anzahl von Katzen als String zurückgibt. Das Format soll dabei z.B. für drei Katzen sein: `Die Anzahl der Katzen: 3`. Die Anzahl der Katzen wird als Parameter im Funktionsaufruf an die Funktion übergeben. <br>**Tipp:** `def cats(count)`<br>
Gibt es 4 und mehr Katzen, soll nicht die Anzahl zurückgegeben werden, sondern der Text `viel zu viele Katzen!`

Lassen Sie `cats(count)` mit folgenden Werten ausführen: 2, 7

## Aufgabe 2: Donaudampfschiffahrtsgesellschaftsstewardess
Schreiben Sie eine Funktion, die das Wort <b>Donaudampfschiffahrtsgesellschaftsstewardess</b> in die einzelnen Buchstaben splittet und in einer Liste sammelt.
1. Welche Länge hat die Liste?
2. Entfernen Sie alle Buchstaben, die doppelt auftauchen. Welche Länge hat die Liste jetzt?


## Aufgabe 3: Buchstaben zählen
Erstellen Sie eine Liste <i>Lieblingstiere</i> und füllen Sie diese mit diesen Tieren. <br ><b>cat, dog, crocodile, bird, elephant, giraffe, stork, worm, warthog, kiwi, kangaroo, snake, monkey</b>
1. Wie viele Tiere sind in Ihrer Liste, die mit 5 und mehr Buchstaben geschrieben werden?<br>
2. Sortieren Sie die Tierliste alphabetisch - von Z nach A.
3. Wie oft taucht der Buchstabe a/A in Ihrer Tierliste auf?


## Aufgabe 4: Tuple sortieren
Erstellen Sie diese Liste: [(1, 9), (3, 2), (31, 3, 1), (4, 33)] und sortieren Sie die Liste aufsteigend nach dem jeweils letzten Element des Tuples. <br>


## Aufgabe 5: Oh, wie schön ist List Comprehension!
Schreiben Sie eine Funktion, die für den Input einer Liste von Zahlen eine Liste identischer Länge und die verdoppelten Zahlen des Inputs zurückgibt.<br>
Beispiel: Input: [1, 2, 3, 4, 5]) <br>
        Output: [2, 4, 6, 8, 10]<br>

## Aufgabe 6: Tuple Addition and maximale Tuple Action
tt = (23, 524, 668, 4, 26, 893, 86)
Ermitteln Sie den höchsten Wert im Tuple `tt` und addieren Sie diesen zum Wert, der den Index 2 im Tuple belegt.
Die Funktion soll das Ergebnis zurückgeben.