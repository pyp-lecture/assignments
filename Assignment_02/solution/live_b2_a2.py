def average(werte):
    sum = 0.0
    anz = 0
    for wert in werte:
        sum = sum + wert
        anz = anz + 1

    return sum / anz

a = average([2, 8, 9, 2, 7, 20])

print(a)
