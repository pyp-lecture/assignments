def fib(n):
    if n == 0:
        ergebnis = 0
    elif n == 1:
        ergebnis = 1
    else:
        ergebnis = fib(n - 1) + fib(n - 2)

    return ergebnis

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
    print("Mega-Fibonacci-Recher (c) TS + TS")
    n = int(input("Gibt mir ein n: "))

    ergebnis = fib_iterativ(n)
    print(f"{n}!= {ergebnis}")

    ergebnis = fib(n)
    print(f"{n}!= {ergebnis}")
