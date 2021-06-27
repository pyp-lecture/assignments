import numpy as np

# AxB=X
A = np.array([[1, 0], [0, 1]], int)
B = np.array([[1, 2], [3, 4]], int)

X = np.dot(A,B)
print(f'X = {X}')

