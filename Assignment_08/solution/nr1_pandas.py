
import matplotlib.pyplot as plt
import pandas as pd


def aufgabe_1a():
    a = pd.read_csv("/Users/Theresa/Documents/python-lecture/blatt8/solution/company_sales_data.csv", usecols= ["total_profit"])

    plt.plot(a)
    plt.xlabel("month_number")
    plt.ylabel("total_profit")
    plt.show()

def aufgabe_2a():
    produkte = ["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]

    b = pd.read_csv("/Users/Theresa/Documents/python-lecture/blatt8/solution/company_sales_data.csv", usecols=produkte)
    plt.xlabel("month_number")
    plt.ylabel("products_sold")

    for key in b.keys(): # wir gehen über die einzelnen columns
        plt.plot(b[key], label = key) # und dann plotten wir sie

    plt.legend()
    plt.show()

if __name__ == "__main__":
    #aufgabe_1a()
    aufgabe_2a()