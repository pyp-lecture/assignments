import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

def index_to_date(index):
    t = dt.timedelta(1 + int(index))
    date = dt.datetime(2021, 6, 23) + t
    return date.strftime('%d.%m')

df = np.vectorize(index_to_date)

celsius_min = np.array([29.6, 24.1, 28.7, 32.3, 29.5, 30.5, 25.8, 19.1])
celsius_max = np.array([31.8, 34.9, 36.3, 33.0, 34.9, 35.6, 29.4, 27.2])
index = np.arange(0, 8)

datum = df(index)
print(datum)

plt.plot(datum, celsius_min, color="b", label='Höchstwerte', marker="*")
plt.plot(datum, celsius_max, color="r", label='Tiefstwerte', marker='*')
#plt.ylim(-273, 2000)
plt.legend() # I am Legend
plt.show()
