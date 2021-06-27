# Aus der Vorlesung
import numpy as np

# [[1, 0], [0, 1]]
# [[1, 2], [3, 4]]

m1 = np.array([[1, 0], [0, 1]])
m2 = np.array([[1, 2], [3, 4]])

e = np.dot(m1, m2)
print(e)