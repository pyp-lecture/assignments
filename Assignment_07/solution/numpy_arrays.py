import numpy as np
import numpy.random as rn
import numpy.linalg as lin


def Matrix(array):
    print(a)
    print(f"Shape: {a.shape}") #1
    print(f"Dimension: {a.ndim}") #2
    print(f"Länge der Elemente in bytes: {a.itemsize}") #3




if __name__ == "__main__":
    
    a = np.random.random((2,4))
    b = np.random.randint(1000,size=(4,2))
    c= (rn.randint(1, 100, 4),rn.randint(1, 100, 4))
    Matrix(a)
    Matrix(b)
    Matrix(c)
    