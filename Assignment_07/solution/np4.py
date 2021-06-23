# Aus der Vorlesung
import numpy as np
import matplotlib.pyplot as mp

# a) x^2 - 4x + 7
# b) x^4 - 11x^3 + 9x^2 + 11x - 10

def fa(x):
    return x**2 - 4*x + 7

def fb(x):
    return x**4 - 11*x**3 + 9*x**2 + 11*x - 10

# [10.+0.0000000e+00j -1.+0.0000000e+00j ]
f1 = np.poly1d([1, -11, 9, 11, -10])
nst1 = f1.roots

# [2.+1.73205081j 2.-1.73205081j]
f2 = np.poly1d([1, -4, 7])
nst2 = np.roots(f2)

xs = np.linspace(-2, 2, 1001)
mp.plot(xs, f1(xs))
mp.plot(xs, xs*0)
mp.show()