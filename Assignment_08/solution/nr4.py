import matplotlib.pyplot as plt
import seaborn as sns

def aufgabe4():
    celsius_min = [29.6, 24.1, 28.7, 32.3, 29.5, 30.5, 25.8, 19.1]
    celsius_max = [31.8, 34.9, 36.3, 33.0, 34.9, 35.6, 29.4, 27.2]

    sns.set_style("darkgrid")

    plt.plot(celsius_min, color = 'blue', label = 'min temp')
    plt.plot(celsius_max, color = 'red', label = 'max temp')
    plt.legend()
    plt.xlabel("Tag")
    plt.ylabel("Temperatur in °C")

    plt.show()

aufgabe4()