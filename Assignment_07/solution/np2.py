# Aus der Vorlesung
import numpy as np
import numpy.linalg as npl

#  x + 3y + 5z = 10
# 2x + 5y +  z =  8
# 2x + 3y + 8z =  3

def f1(x, y, z):
    return x + 3*y + 5*z - 10

def f2(x, y, z):
    return 2*x + 5*y + z - 8

def f3(x, y, z):
    return 2*x + 3*y + 8*z - 3

A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
e = np.array([10, 8, 3])
print(A)
print(e)

v = npl.solve(A, e)
x = v[0]
y = v[1]
z = v[2]

print(f"Lösung des GS: x={x}, y={y}, z={z}")

print(f1(v[0], v[1], v[2]))
print(f2(v[0], v[1], v[2]))
print(f3(v[0], v[1], v[2]))
