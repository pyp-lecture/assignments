def fib1(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:

        z=fib1(n-1)+fib1(n-2)
        return z

def fib_iterativ(n):
    ergebnis = 0

    if n == 0:
        ergebnis = 0
    elif n == 1:
        ergebnis = 1
    else: # n >=2
        ergebnis_n_0 = 0 # aktuelle Wert
        ergebnis_n_1 = 1 # Vorgänger
        ergebnis_n_2 = 0 # Vorvorgänger

        for i in range(2, n+1):
            # Fibonacci Karnickel Regel
            ergebnis_n_0 = ergebnis_n_1 + ergebnis_n_2

            # Alles einen verschieben
            ergebnis_n_2 = ergebnis_n_1
            ergebnis_n_1 = ergebnis_n_0

        ergebnis = ergebnis_n_0

    return ergebnis


if __name__ == "__main__":
    n=input("Geben Sie ein n ein")
    m=fib1(int(n))
    print(m)

    print("Iterative Variante - schneller aber komplizierter")
    m=fib_iterativ(int(n))
    print(m)