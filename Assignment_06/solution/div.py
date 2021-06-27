def div(nenner, zähler):                                # Aufgabe 2
    try:
        return zähler / nenner
    except ZeroDivisionError:
        print("Der Nenner darf nicht 0 sein.")


def divi(nenner, zähler):                               # Aufgabe 3
    if nenner == 0:
        raise ZeroDivisionError('Are you dumb?') # Hihi :)
    return zähler / nenner
    
if __name__ == "__main__":
    print(div(3,9))
    print(div(0,3))
    print(div(4,0))

    print(divi(3,9))
    print(divi(0,3))
    print(divi(4,0))