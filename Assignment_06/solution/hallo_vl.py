# Beispiel aus der VL
class NameZuKurzError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ist zu kurz. Bitte mind. 2 Zeichen."

class NameIstZahlError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ist eine Zahl! So heißt doch niemand."


print("Happy greeter (C) TS TS")
name = input("Bitte geben Sie Ihren Namen ein: ")

try:
    name_als_zahl = int(name)
except:
    pass
else:
    raise NameIstZahlError("Name darf keine Zahl sein")

if len(name) <= 2:
    raise NameZuKurzError(name)
else:
    print(f"Hallo {name}")
