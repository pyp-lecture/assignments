# Aus der Vorlesung
import numpy as np
import matplotlib.pyplot as plt

product_categories = {
    'facecream': 1,
    'facewash': 2,
    'toothpaste': 3,
    'bathingsoap': 4,
    'shampoo': 5,
    'moisturizer': 6,
}

data = np.loadtxt('company_sales_data.csv', int, '#', ',', None, 1)
total_profit = data[:, 8]
year = data[:, 0]

#plt.bar(year, total_profit)
#plt.show()

for categrory, index in product_categories.items():
    total_units = data[:, 7]
    categrory_data = data[:, index] / total_units
    plt.plot(year, categrory_data, label=categrory)

plt.legend()
plt.show()