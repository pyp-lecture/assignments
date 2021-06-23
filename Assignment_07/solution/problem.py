# Läsen eines LGS mit Numpy – super kommentiert von Team 01!
import numpy as np
import numpy.linalg as la

# LGS:
# 1x + 3y + 5z = 10
# 2x + 5y + 1z = 8
# 2x + 3y + 8z = 3

# Umschreiben in Matrixschreibweise in der Form Ax = b
A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]],int)
b = np.array([10, 8, 3],int)


# Lösen mit dem solve-Befehl
x = la.solve(A,b)
print(f'x = {x[0]}\ny={x[1]}\nz={x[2]}')