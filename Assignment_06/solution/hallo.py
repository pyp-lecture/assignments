
## Version 1
# :
class BuchstabenError(Exception):
    pass

class ZahlenError(Exception):
    pass


def funk(name):
    if len(name)<3:
        raise BuchstabenError('Zu wenige Buchstaben!')
    elif any(i.isdigit() for i in name):
        raise ZahlenError('Zahlen sind als Eingabe nicht erlaubt!')
    return print(f'Hallo, {name}!')


name = str(input("Geben Sie Ihren Vornamen an: "))
funk(name)

## Version 2:
class LengthError(Exception):
    pass

class DigitError(Exception):
    pass

def hallo(name):
    try:
        if name.isdigit():
            raise DigitError()
        if (len(name) <= 2):
            raise LengthError()
        return ('Hallo, '+ name + '!')
    except LengthError:
        return('Einen so kurzen Namen gibt es nicht!')
    except DigitError:
        return('Zahlen sind keine Namen!')

def name_fragen():
    name = input('Bitte gib Deinen Namen ein: ')
    return name
        
print(hallo(name_fragen()))