import numpy as np
import numpy.random as rn
import numpy.linalg as lin

def Matrix(array):
    print(a)
    print(f"Shape: {a.shape}") #1
    print(f"Dimension: {a.ndim}") #2
    print(f"Länge der Elemente in bytes: {a.itemsize}") #3

if __name__ == "__main__":
    a = np.random.random((4,2))
    b = np.random.randint(1000,size=(4,2))
    c= (rn.randint(4, 100, 1),rn.randint(4, 100, 1))
    d = np.array([[1,2], [3,4],[5,6],[7,8]])
    Matrix(a)
    Matrix(b)
    Matrix(c)
    