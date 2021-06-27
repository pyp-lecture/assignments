import numpy as np


def ersetzen(arr):
    z=-1
    for i in arr:
        z+=1
        if i%2!=0:
            arr[z]=-1

    print(arr)

if __name__ == "__main__":
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9])
    ersetzen(arr)