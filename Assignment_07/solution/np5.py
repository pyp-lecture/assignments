# Aus der Vorlesung
import numpy as np

vfilter = np.vectorize(lambda x : -1 if x %2 == 1 else x)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
new = vfilter(arr)

print(new)
