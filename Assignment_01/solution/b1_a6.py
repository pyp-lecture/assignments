import math

def is_prim(z):
    i = 2
    while i < math.ceil(math.sqrt(z)):
        if z % i == 0:
            return False
        i = i + 1

    return True

i = 2
while i <= 100:
    if is_prim(i):
        print(i)
    i = i + 1
