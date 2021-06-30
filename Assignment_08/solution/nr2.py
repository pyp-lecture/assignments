class myfault(Exception):
        pass

def c2f(c):
    a = int(c)
    f = ((9*a)/5)+32
    return f

def c2k(c):
    a = int(c)
    if a < -273.15:
        raise myfault("Physikalisch unmöglich!")
    k = a + 273.15
    return k

def f2c(f):
    a = int(f)
    c = 5*(a-32)/9
    return c

def f2k(f):
    a = int(f)
    if a < -459.67:
        raise myfault("Physikalisch unmöglich!")
    k = (5*(a-32)/9)+273.15
    return k


f = c2f(57)
print(f)

k = c2k(98)
print(k)

c = f2c(120)
print(c)

k = f2k(35)
print(k)