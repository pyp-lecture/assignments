# Blatt 2: Grundlagen und Funktionen

*Fällig: 11.05.2021*

## Aufgabe 1: Zahlenraten
Schreiben Sie ein Programm, dass sich eine Zahl zwischen 1 und 100 ausdenkt

```python
import random
zahl = random.randrange(1, 101)
```

  * Der Benutzer muss versuchen die Zahl zu raten. Er oder sie bekommt die Auskunft, ob sein Wert zu hoch oder zu niedrig liegt.
  * Beim Raten der richtigen Zahl wird die Anzahl der Versuche ausgegeben.

**Beispielausgabe**<br>
Ihre Zahl: 50<br>
Zu niedrig<br>
Ihre Zahl: 75<br>
Zu niedrig<br>
Ihre Zahl: 85<br>
Zu niedrig<br>
Ihre Zahl: 90<br>
Zu hoch<br>
Ihre Zahl: 87<br>
Richtig nach 5 Versuchen<br>

**Abgabe:** b2_a1.py

##  Aufgabe 2: Arithmetisches Mittel

Berechnen Sie das arithmetische Mittel einer Reihe von Zahlen. Die Daten werden als Tuple gegeben.

Schreiben Sie eine Funktion `average`, die diese Aufgabe ausführt und die Anzahl der Werte und den Durchschnitt zurückgibt.

Testen Sie Ihre Funktion mit folgenden Werten (2, 8, 9, 2, 7, 20)

**Abgabe:** b2_a2.py

## Aufgabe 3: Sieb des Eratosthenes

Implementieren Sie das [Sieb des Eratosthenes](https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes).

kleiner Tipp: `from math import sqrt`

Berechnen Sie die Primzahlen bis 1000. Verwenden Sie ein Array für die gestrichenen Zahlen.

**Abgabe:** b2_a3.py

## Aufgabe 4: Addition

Schreiben Sie ein kurzes Programm, dass alle geraden Zahlen von 1 bis 100 addiert und das Ergebnis ausgibt.

Es soll möglich sein, das Programm ohne weitere Parameter aufzurufen:

`$ ./b2_a4.py`

Und die Ausgabe soll etwas in der Art sein: `2570`

**Abgabe:** b2_a4.py