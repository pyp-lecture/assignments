# Blatt 8: Matplotlib

*Fällig: 29.06.2021*

## Aufgabe 1: Schaubilder
Lesen Sie die Datei `company_sales_data.csv` ein und speichern Sie die Graphen als `.jpg`-Dateien ab
1. Erzeugen Sie einen Graphen, auf dem man den `total_profit` pro Monat ablesen kann.
2. Erzeugen Sie einen Graphen in dem Sie für die verschiedenen Produktkategorien die Verkaufszahlen pro Monat abbilden (pro Kategorie eine Linie)

Abgabe: b8_a1.py, b8_a1_1.jpg b8_a1_2.jpg

## Aufgabe 2: Kelvin und Celsius
Schreibe 3 Funktionen, die Temperaturen in verschiedenen Skalensysteme umwandeln.

*Tipps zur Umrechnung:*
```
Celsius = 5/9 * (Fahrenheit - 32).
Celsius = Kelvin - 273.15.
Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K
```

Es soll zum Test umgewandelt werden:
```
57 Celsius in Fahrenheit
98 Celsius in Kelvin
120 Fahrenheit in Celsius
35 Fahrenheit in Kelvin
```


## Aufgabe 3:
```
[[1143, 0], [320, 48], [2314, 22]]
[[123, 2111], [33, 41], [2999, 2861]]
```
Berechnen Sie jeweils:
1. die kummulative Summe entlang der ersten Spalte
2. Das Minimum, das Maximum
3. Das Kreuzprodukt

## Aufgabe 4:
Die letzten Tage war es leider sehr heiß. Plotten Sie die Temaratur Hoch- und Tiefwerte  für die letzen 8 Tage in einem Diagramm. Achten Sie auf eine Legende (Hochwerte: rot, Tiefwerte: blau).
```
celsius_min = [29.6, 24.1, 28.7, 32.3, 29.5, 30.5, 25.8, 19.1]
celsius_max = [31.8, 34.9, 36.3, 33.0, 34.9, 35.6, 29.4, 27.2]
```
