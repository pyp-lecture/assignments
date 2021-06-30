
#Lesen Sie die Datei company_sales_data.csv ein. und speichern Sie die Graphen als .jpg-Dateien ab

#    Erzeugen Sie einen Graphen auf dem man den total_profit pro Monat ablesen kann.
#    Erzeugen Sie einen Graphen in dem Sie für die verschiedenen Produktkategorien die Verkaufszahlen pro Monat abbilden (pro Kategorie eine Linie)


import numpy as np
import matplotlib.pyplot as plt

figure, axis = plt.subplots()


# Daten Importieren
data = np.loadtxt("/Users/Theresa/Documents/python-lecture/blatt8/solution/company_sales_data.csv", int, '#', ',', None, 1)
total_profit = data[:,8]
year = data[:,0]
print(year)

#plt.bar(year, total_profit)
#plt.show()

product_categories = {'facecream':1, 'facewash':2, 'toothpaste':3, 'bathingsoap':4, 'shampoo':5, 'moisturizer':6}

for product, index in product_categories.items():
    category_data = data[:, index]
    plt.plot(year, category_data, label=product)
plt.legend()
plt.show()
