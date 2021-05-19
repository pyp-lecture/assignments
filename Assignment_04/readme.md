# Blatt 4: Dictionaries, Sets and Strings

*Fällig: 01.06.2021*

## Aufgabe 1:  Wörterbuch
Schreiben Sie eine Funktion de_en, die deutsche Fachbegriffe in englische übersetzt. Speichern Sie ihr Wörterbuch in einer geeigneten Datenstruktur.<br> 
Folgende Übersetzungen sollen möglich sein:<br>
Antriebsritzel ↔ drive pinion<br>
Biegeeigenschaft ↔ bending property<br>
Drehklappe ↔ butterfly valve<br>
Istspiel ↔ actual clearance<br>
Keilriemen ↔ V-belt<br>
Testen Sie die Funktion mit den Testwerten: Keilriemen und butterfly valve<br>

## Aufgabe 2: Gaius Iulius Caesar
Erstellen Sie ein Dictionary, in dem die Keys für die Position im folgenden Satz stehen. Als Values stehen die einzelnen Worte.<br>
<b>Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appellantur.</b>
<br>
1. Wie viele Buchstaben enthält der Text insgesamt?
2. Betrachten Sie jede Hälfte des Satzes. Welcher Teil enthält mehr Vokale?

## Aufgabe 3: Halb, halb
1. Schreiben Sie eine Funktion, die Strings in der Hälfte teilt. Ist die Länge des Strings gerade, sind die Hälften gleich lang. Bei ungerader Länge, gehört der extra Buchstabe zum ersten Teilstring.<br>
Beispiel: 'abcde', die vordere Hälfte 'abc', die hintere Hälfte ist 'de'.<br>
2. teilen('abcd', 'xy'), 'abxcdy')
Erhält die Funktion 2 Strings (String a und String b) als Input, soll der Output so gestaltet sein: a-vorne + b-vorne + a-hinten + b-hinten -> abxcdy

## Aufgabe 4: Aus 2 mach 1
Verbinden Sie die beiden dicitonaries zu einem.<br>
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}<br>
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}<br>

## Aufgabe 5: Gehaltserhöhung
Übernehmen sie das `payDict` und schreiben Sie eine Funktion, mit der das Gehalt eines Mitarbeiters angepasst werden kann. Die Funktion soll als Input den Namen des anzupassenden Mitarbeiters und das neue Gehalt nehmen
changePay(Karen, 8000).<br>
``` payDict = {
     'emp1': {'name': 'Karen', 'salary': 7500},
     'emp2': {'name': 'Steph', 'salary': 8000},
     'emp3': {'name': 'Cynthia', 'salary': 6500}
     'emp4': {'name': 'Paul', 'salary': 4500}
     'emp5': {'name': 'Myriam', 'salary': 180000}
     'emp6': {'name': 'Steven', 'salary': 2500}
     'emp7': {'name': 'Astrid', 'salary': 6500}
     'emp8': {'name': 'David', 'salary': 1000}
     'emp9': {'name': 'Melanie', 'salary': 2340}
} 
```
Erhöhen Sie jeweils das Gehalt von Stefen, Melanie, David und Astrid um 500. Welchen Gehaltsdurchschnitt gibt es dann in diesem Unternehmen?

## Aufgabe 6: Gemeinsamkeiten behalten
Entfernen Sie alle Elemente in set1, die set1 und set2 nicht gemeinsam haben. <br>set1 = {10, 20, 30, 40, 50}<br>
set2 = {30, 40, 50, 60, 70}<br>

## Aufgabe 7: Hello again, Donaudampfschiffahrtsgesellschaftskapitän
Schreiben Sie eine Funktion, die das Wort <b>Donaudampfschiffahrtsgesellschaftskapitän</b> zurückgibt aber Buchstaben, die ein zweites Mal verwendet werden durch * ersetzt. <br>
Beispiel: Schifffahrt -> Schif**a*rt