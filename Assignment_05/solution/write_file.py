f = open("ueber_mich.txt", "r")
inhalt = f.readlines()

for zeile in inhalt:
    print(zeile)

f.close()

lieblingsfilm = input("Lieblingsfilm: ")
lieblingsspiel = input("Lieblingsspiel: ")

inhalt.append(f"Lieblingsfilm : {lieblingsfilm}\n")
inhalt.append(f"Lieblingsspiel: {lieblingsspiel}\n")

f = open("ueber_mich.txt", "a")

f.write(f"Lieblingsfilm: {lieblingsfilm}\n")
f.write(f"Lieblingsspiel: {lieblingsspiel}\n")

f.close()
