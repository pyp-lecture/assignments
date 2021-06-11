FACTOR = 1.35962

kw = float(input('Bitte geben Sie die Leistung in kW an: '))
ps = kw * FACTOR

print('Die Leistung beträgt ' + str(kw) + ' kW = ' + str(ps) + ' PS')
