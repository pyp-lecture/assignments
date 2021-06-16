# Beispiel aus der VL
class DuBistZuDummZumRechnenError(Exception):
    def __init__(self, a, b, s):
        self.a = a
        self.b = b
        self.s = s

    def __str__(self):
        return f"{self.s}: a={self.a}, b={self.b}"

def div2(a, b):
    if b == 0:
        raise ZeroDivisionError()

    return a / b

def div(a, b):
    if a < 0 or b < 0:
        raise DuBistZuDummZumRechnenError(a, b, "Doch keine negativen Zahlen, wir sind erst in der 2. Klasse")
    try:
        return a / b
    except ZeroDivisionError:
        raise DuBistZuDummZumRechnenError(a, b, "Durch 0 kann man nicht teilen")

if __name__ == "__main__":
    a = int(input("Gib mir a: "))
    b = int(input("Gib mir b: "))
    ergebnis = div(a, b)
    print(f"{a} / {b} = {ergebnis}")


class DataFormatError:
    pass

def get_data():
    return (0, 0)

def read_data(filename):
    f = open(filename, "r")

    try:
        a, b = get_data(f)
        c = a / b
    except ZeroDivisionError:
        raise DataFormatError()

    f.close()

def get_file():
    filename = input("Dateiname: ")
    try:
        read_data(filename)
    except FileNotFoundError:
        print("Datei existiert nicht")
    except IOError:
        print("Datei existiert aber kann nicht gelesen werden")

get_file()