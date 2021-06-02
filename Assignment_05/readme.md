# Blatt 5: Input und Output, Klassen

*Fällig: 08.06.2021*

## Aufgabe 1: Zwei schecklich nette Ungeheuer
Sie werden eine Klasse <b>ungeheuer</b> schreiben, welche von object erbt. Diese soll möglichst generell für alle Arten von Ungeheuern funktionieren. 
1. Schreiben Sie das Gerüst der Klasse ungeheuer mit den Klassenvariablen `horrible = True (int)` und den **Instanzvariablen** `size [Größe in cm] (Typ Integer, public),` `__vulnerability [Schwachstelle] (Typ String, private)` und `number_of_victims [Anzahl Opfer] (Typ Integer, private)`. Letzteres soll als Default-Argument eine 0 erhalten.
2. Verstecken Sie mithilfe des property-Dekorators die Instanzvariable `number_of_victims` und erlauben gleichzeitig dadurch den Zugriff und die Änderung der Variablen von außen.
3.  Schreiben Sie eine Methode `grow(int size) -> None` innerhalb der Klasse, welche einen Parameter size vom Typ Integer enthält. Dieser soll die Instanzvariable `size` um seinen Wert erhöhen.
4.  Schreiben Sie eine weitere Methode `scare() -> bool`, welche erschrecken kann. Das Ungeheuer soll aber nur erschrecken können, wenn es mindestens einen halben Meter groß ist. Die Rückgabe, ob ein Erschrecken geklappt hat, ist ein simples True oder False. Falls es erfolgreich erschrecken konnte, soll sich zudem `number_of_victims` um eins erhöhen.
5.  Denken Sie sich eine weitere Klassenmethode `methodenname(str target) -> bool` aus, die Schaden nimmt, wenn man die Schwachstelle errät/trifft/... Das Ungeheuer soll dann um 10 cm schrumpfen und bei einem Treffer `True` zurückgeben, ansonsten `False`.
6.  Dokumentieren Sie alles.
7. Instanziieren Sie im Block `if __name__ == "__main__"` ein Ungeheuer `nightstalker` aus der Klasse <b>ungeheuer</b> mit den Werten `size = 50 `und `vulnerability = "heel"` und ein weiteres `baby_monster` mit den Werten `size = 20` und `vulnerability = "head"`. Lassen Sie beide Ungeheuer nun Ihren Schrecken `scare()` verbreiten. Anschließend soll versucht werden, den beiden Ungeheuern am Kopf `head` Schaden zuzufügen.

## Aufgabe 2: Input und Output 
Erstellen Sie mit Python eine `.txt`-Datei im Ordner ihrer `.py`-Abgabedatei. Diese soll einige Informationen über Sie erhalten. 
```
Ihr Vorname
Ihr Nachname
Mein Lieblingslied ist:
Ich esse gerne:
```
Schreiben Sie nun ein Programm ``, welches diese Datei einliest. 
1. Fügen Sie eine Funktion hinzu, die eine weitere Zeile ergänzt. Nutzen Sie hierfür den Input die Kommandozeile (Idee: Die Funktion könnte Sie nach Ihren Lieblingsfilm fragen).
2. Schreiben Sie eine weitere Funktion die den neuen Inhalt in die `.txt`-Datei schreibt. 