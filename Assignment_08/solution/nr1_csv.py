
#Aufgabe 1: Schaubilder

#Lesen Sie die Datei company_sales_data.csv ein. und speichern Sie die Graphen als .jpg-Dateien ab

#    Erzeugen Sie einen Graphen auf dem man den total_profit pro Monat ablesen kann.
#    Erzeugen Sie einen Graphen in dem Sie für die verschiedenen Produktkategorien die Verkaufszahlen pro Monat abbilden (pro Kategorie eine Linie)

#Abgabe: b8_a1.py, b8_a1_1.jpg b8_a1_2.jpg

import numpy as np
import matplotlib.pyplot as plt

figure, axis = plt.subplots()


# Daten Importieren
data = np.loadtxt("/Users/Theresa/Documents/python-lecture/blatt8/solution/company_sales_data.csv")

# Liste mit überschrifen
y_label=["month_number", 	"facecream", 	"facewash", 	"toothpaste", 	"bathingsoap", 	"shampoo", 	"moisturizer", 	"total_units", 	"total_profit"]
x_label=y_label[0]

# Aufgabe 1
def a1(x,y):
    xx=[]
    yy=[]
    for row in data:
        xx.append(row[x])
    
    for row in data:
        yy.append(row[y])

    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label[y])
    axis.set_title(y_label[y])
    
    plt.bar(xx,yy,0.9)
    plt.savefig('b8_a1.jpg')
    plt.show()


# Aufgabe 2
def a2(x,y,y_end):

    xx=[]   #Liste für x werte
    yy=[]   # Liste für y Werte

    # Ausstieg aus Rekursion
    if y==y_end+1:

        plt.xlabel(y_label[0])
        plt.ylabel("verkaufte einheiten")
        plt.title("Produktbeitrag zum Unternehmenserfolg")
        
        plt.legend()
        plt.savefig('b8_a2.jpg')
        plt.show()
        return     

    for row in data:
        xx.append(row[x])
    
    for row in data:
        yy.append(row[y])  
    
    plt.plot(xx, yy, label=str(y_label[y]))
    return a2(x, y+1, y_end)
    
if __name__ == "__main__":

    a1(0,8)     # x- Achse, yachse
    a2(0,1,6)   # x-Achse, y-Achse, y-ende


