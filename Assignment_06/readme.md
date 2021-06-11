# Blatt 6: Rekursion, Ausnahmen und Tests

*Fällig: 15.06.2021*

## Aufgabe 1: Fibonacci
Die Fibonacci-Folge ist eine unendliche Zahlenfolge (0, 1, 1, 2, 3, 5, 8 ...). Die ersten Terme sind 0 und 1. Alle folgenden Terme können berechnet werden, wenn die vorangehenden zwei addiert werden. Dies bedeutet, dass der Term n die Summe der Terme (n-1) und (n-2) ist, also ganz allgemein: f(n) = f(n - 1) + f(n - 2) mit f(0)=0 und f(1)=1

1. Schreiben Sie eine Funktion `fib`, mit der die Fibonnacci-Folge berechnet werden kann. Nutzen Sie dafür **Rekursion**. Tipp: STR+C bricht das laufende Programm ab.
2. Gestalten Sie ihre Abgabe so, dass der Nutzer nach dem `n` gefragt wird, das berechnet werden soll.

## Aufgabe 2: You can't devide through 0
Schreiben Sie eine Funktion `div`, die eine Zahl durch eine andere teilt. Um zu vermeiden, dass beim Teilen durch 0 ein Error geworfen wird, nutzen Sie `try .. except`, um den Fehler innerhalb der Funktion abzufangen und einen "vernünftigen" Wert zurückzugeben.

## Aufgabe 3: Vorbeigehen
Nehmen Sie an, dass es Ihnen nun egal ist, dass man nicht durch 0 teilen kann und dass Sie den Benutzer doch wieder für seine Dummheit bestrafen wollen. Fangen Sie den Fehler weiterhin, geben ihn dann aber an den Benutzer weiter. Nutzen Sie eine geeignete Exception.

## Aufgabe 4: Hallo!
Schreiben Sie eine Funktion, die Ihren Vornamen über die Kommandozeile abfragt und sie dann mit einer Textausgabe begrüßt.
1. Gestalten Sie die Funktion so, dass Sie eine Exception werfen, wenn Ihr Name zwei und weniger Buchstaben hat.
2. Welche Exception würden Sie verwenden, wenn Sie fälschlich eingegebene Zahlenwerte abfangen wollen?
