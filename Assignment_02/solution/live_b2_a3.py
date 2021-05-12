import math

grenze = 1000
a = [ False ] * grenze

def gestrichen(z, arr):
    return arr[z - 1]

def streiche(z, arr):
    arr[z - 1] = True

def print_prim(arr):
    for i in range(2, grenze):
        if not gestrichen(i, arr):
            print(i)

for n in range(2, grenze + 1):
    for k in range(n, grenze + 1):
        p = n * k
        if p <= grenze:
            streiche(p, a)

print_prim(a)

#print(str(a))