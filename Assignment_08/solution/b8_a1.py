#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np


def read_data():
    data = {
        'month_number': [],
        'facecream': [],
        'facewash': [],
        'toothpaste': [],
        'bathingsoap': [],
        'shampoo': [],
        'moisturizer': [],
        'total_units': [],
        'total_profit': []
    }
    count = 0
    for i in data:
        data[i] = np.loadtxt('company_sales_data.csv',
                             delimiter=',',
                             usecols=(count),
                             skiprows=1)
        count += 1
    return data


def main():
    data = read_data()
    plt.plot(data['month_number'], data['total_profit'], label='totoal_profit')
    plt.xlabel('Monat')
    plt.ylabel('CA$H')
    plt.legend(loc='best')
    plt.savefig('b8_a1_1.jpg')
    plt.clf()

    for i in range(1, 7):
        #print(list(data.keys()))
        plt.plot(data['month_number'],
                 data[list(data.keys())[i]],
                 label=list(data.keys())[i])
    plt.xlabel('Monat')
    plt.ylabel('Verkaufszahlen')
    plt.legend(loc='best')
    plt.savefig('b8_a1_2.jpg')
    return 0


if __name__ == "__main__":
    main()
