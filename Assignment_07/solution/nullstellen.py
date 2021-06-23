import numpy as np

# Funktionen Programmeiren 
f1=np.poly1d([1,-4,7])
f2=np.poly1d([1,-11,9,11,-10])

# Nullstellen suchen und abspeichern
a=np.roots(f1)
b=np.roots(f2)

# Nullstellen benutzerferundlich ausgeben
z=0
print('Nullstellen von a)')
for x in a:
    z += 1
    print(f'{z}) {x}')
z=0
print('Nullstellen von b)')
for x in b:
    z += 1
    print(f'{z}) {x}')
#######################
def Nullstellen():
    a = np.array([1,-4,7])
    b = np.array([1,-11,9,11,-10])

    p1 = [1,-4,7]
    a0 = np.roots(p1)
    p2 = [1,-11,9,11,-10]
    b0 = np.roots(p2)

    print(f"Nullstellen a: {a0}")
    print(f"Nullstellen b: {b0}")

Nullstellen()
############################
# Nullstellensuche ganz geschickt gelöst

import matplotlib.pyplot as plt

x = np.linspace(-3, 13, 10001)
#y = x**2-4*x+7
y=x**4-11*x**3+9*x**2+11*x-10

xAchse=0*x
plt.plot(x,xAchse,'k')
plt.plot(x, y)
plt.show()

def ns_suche(x,y):
    liste=[]
    zaehler=-1
    for i in y:
        zaehler+=1
        if i==0:
            liste.append(x[zaehler])
    if len(liste)==0:
        return print('Keine Nullstellen gefunden!')
    else:
        return print('Nullstelle bei x=',liste)

ns_suche(x,y)