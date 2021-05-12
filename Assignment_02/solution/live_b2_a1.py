import random

zahl = random.randrange(1, 101)
versuche = 1

while True:
    tipp = int(input("Ihre Zahl: "))

    if tipp < zahl:
        print("Zu niedrig")
    elif tipp > zahl:
        print("Zu hoch")
    else:
        break

    versuche = versuche + 1

# Hier kommt man nur mit richtigem Raten hin!
print("Richtig - du bist ein Pro! Versuche: " + str(versuche))