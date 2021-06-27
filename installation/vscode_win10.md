# Visual Studio Code unter Windows 10 installieren

Diese Anleitung zeigt Ihnen, wie Sie Visual Studio Code installieren können. Bitte installieren Sie __vorher__ Python 3.9 gemäß der [Anleitung](python_win10.md).

## Download

Laden Sie Visual Studio Code von der [Webseite](https://code.visualstudio.com) `https://code.visualstudio.com` herunter. Klicken Sie auf __Download for Windows__ und speichern Sie das Installationsprogramm auf Ihrem Rechner.

<img src="img/vscode_1.png" width="700">
<br>
<img src="img/vscode_2.png" width="400">

## Installationsprogramm

Führen Sie das Installationsprogramm aus dem Download-Ordner durch Doppelklick aus.

<img src="img/vscode_3.png" width="600"><br>
<img src="img/vscode_4.png" width="400">

Akzeptieren Sie die Lizenzvereinbarung.
Klicken Sie auf __Weiter__.

<img src="img/vscode_5.png" width="500">

Den Installationspfad und Startmenü-Ordner müssen Sie nicht anpassen. Klicken Sie auf __Weiter__.

<img src="img/vscode_6.png" width="500">
<img src="img/vscode_7.png" width="500">

Setzen Sie bei dem Dialog __Zusätzliche Aufgaben wählen__ alle Häckchen. Klicken Sie auf __Weiter__.

  * [X] Desktop-Symbol erstellen
  * [X] Aktion "Mit Code öffnen" dem Dateikontextmenü von Windows-Explorer hinzufügen
  * [X] Aktion "Mit Code öffnen" dem Verzeichniskontextmenü von Windows-Explorer hinzufügen
  * [X] Code als Editor für unterstützte Dateitypen registrieren
  * [X] Zu PATH hinzufügen (nach Neustart verfügbar)


<img src="img/vscode_8.png" width="500">

Klicken Sie auf __Installieren__.

<img src="img/vscode_9.png" width="500">

Die Installation sollte jetzt durchlaufen.

<img src="img/vscode_10.png" width="400">

Nach Abschluss des Assistenten setzen Sie das Häkchen bei __Visual Studio Code starten__.

<img src="img/vscode_11.png" width="500">

## Visual Studio Code konfigurieren

Visual Studio Code startet. Wählen Sie ein Farbschema, das Ihnen gefällt.

<img src="img/vscode_12.png" width="600">

Klicken Sie auf __Browse Language Extensions__.

<img src="img/vscode_13.png" width="700">

Wählen Sie __Python__ aus und klicken Sie auf __Install__.

<img src="img/vscode_14.png" width="700">

Warten Sie, bis die Installation durchgelaufen ist und schließen Sie dann den Tab __Extension: Python__ durch Klick auf das `X`.

Schließen Sie danach auch den Tab __Getting Started__.

<img src="img/vscode_15.png" width="700">

## Test der Installation

Legen Sie mit `File -> New file` eine neue leere Datei an und geben Sie folgenden Inhalt ein:

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,1001)
y = x**2
plt.plot(x, y)
plt.show()
```

Speichern Sie die Datei an einem beliebigen Ort und geben Sie ihr die Dateiextension `.py`, z.B. `test.py`.

<img src="img/vscode_16.png" width="500">

Klicken Sie auf den __Play Button__ oben rechts. Sie sollten jetzt den Plot einer x^2 Funktion sehen.

<img src="img/vscode_17.png" width="500">

Sie haben Visual Studio Code erfolgreich installiert.
