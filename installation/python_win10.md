# Python 3.9 unter Windows 10 installieren

Diese Anleitung zeigt Ihnen, wie Sie Python 3.9, inklusive `pip` und der Bibliotheken `matplotlib` und `numpy` unter Windows 10 installieren.

## Download

Gehen Sie auf die [Webseite](https://python.org) `https://python.org` und laden Sie die aktuelle Version von Python für Windows herunter.

<img src="img/python_1.png" width="700">

Speichern Sie den Download in Ihrem Download-Ordner.

<img src="img/python_2.png" width="300">
<img src="img/python_3.png" width="400">


## Installation von Python

Gehen Sie in den Download-Ordner und starten Sie die Installation durch Doppelklick auf die Installationsdatei.

<img src="img/python_4.png" width="600">

Bestätigen Sie, dass Sie die Datei ausführen möchten.

<img src="img/python_5.png" width="350">

Wenn Sich der Dialog des Installations-Programms öffnet, setzen Sie einen Haken bei __Add Python 3.9 to PATH__ und klicken Sie dann auf __Customize installation__.

<img src="img/python_6.png" width="500">

Bei der Anzeige der optionalen Features, sollten alle Häkchen gesetzt sein:

  * [X] Documentation
  * [X] pip
  * [X] tcl/tk and IDLE
  * [X] py launcher
  * [X] for all users (requires elevation)

Klicken Sie auf __Next__.

<img src="img/python_7.png" width="500">

In den Advanced Options wählen Sie folgendes aus:

  * [X] Install for all users
  * [X] Associate files with Python (requires py launcher)
  * [X] Create shortcuts for installed applications
  * [X] Add Python to environment variables
  * [X] Precompile standard library

Klicken Sie auf __Install__.

<img src="img/python_8.png" width="500">

Bestätigen Sie, dass Python Änderungne an Ihrem System vornehmen darf.

<img src="img/python_9.png" width="300">

Die Installation läuft jetzt durch.

<img src="img/python_10.png" width="400">

Am Ende wird "Setup was successful" angezeigt. Klicken Sie in diesem Dialog auf __Disable path length limit__.

<img src="img/python_11.png" width="500">

Es erfolgt eine erneute Sicherheitsabfrage von Windows. Die Sie wieder mit __Ja__ bestätigen.

<img src="img/python_12.png" width="300">

Jetzt wird angezeigt, dass die Installation erfolgreich war. Schließen Sie das Fenster.

<img src="img/python_13.png" width="400">

## Installation von PIP und den Bibliotheken

Klicken Sie nun auf das Windows-Logo und navigieren See zu __Windows-System__. Klicken Sie auf das Ordnersymbol und klicken Sie dann mit der __RECHTEN__ Maustaste auf __Eingabeaufforderung__. Es erscheint ein Kontextmenü, in dem Sie `Mehr > Als Administrator ausführen` wählen.

<img src="img/python_22.png" width="500">

Es erscheint eine Sicherheitsabfrage von Windows, die Sie wieder mit __Ja__ bestätigen. Erscheint diese nicht, überprüfen Sie bitte, ob Sie oben wirklich mit der RECHTEN Maustaste geklickt haben (Tipp: Rechts ist da, wo nichts links ist.)

<img src="img/python_20.png" width="300">

Es öffnet sich die Windows-Eingabeaufforderung im Administratormodus.

<img src="img/python_26.png" width="500">

Geben Sie folgendes Kommando ein (`C:\Windows\system32>` wird vom System angezeigt und ist nicht Teil Ihrer Eingabe):

```console
C:\Windows\system32> python -m pip install --upgrade pip
```

Sie sehen die Ausgabe, dass `pip` auf die neuste Version gehoben wird.

<img src="img/python_21.png" width="600">

Geben Sie jetzt im selben Fenster folgendes ein:

```console
C:\Windows\system32> pip install matplotlib numpy
```

Sie sollten die Ausgabe sehen, dass die beiden Bibliotheken installiert wurden.

<img src="img/python_25.png" width="600">

Schließen Sie das Fenster der Eingabeaufforderung und klicken Sie erneut auf das Windows-Logo.

## Test der Installation
Gehen Sie im Startmenü auf __Python 3.9__, klicken Sie auf das Ordnersymbol und wählen dann __Python 3.0 (64-bit)__ aus.

<img src="img/python_14.png" width="200">

Es öffnet sich die Python REPL.

<img src="img/python_27.png" width="600">

Zum Testen tippen Sie jetzt folgendes ein (`>>>` ist nicht Teil Ihrer Eingabe, sondern das Prompt von Python):

```console
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x = np.linspace(-10,10,1001)
>>> y = x**2
>>> plt.plot(x, y)
>>> plt.show()
```

Wenn alles richtig installiert wurde, sehen Sie jetzt einen Plot der Funktion x^2 im Bereich -10 bis 10 auf Ihrem Bildschirm.

<img src="img/python_24.png" width="700">

__GESCHAFFT!!__