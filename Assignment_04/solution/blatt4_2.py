# Beispiellösung: Prof. Smits

vokale = { 'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

def vokale_in_woertern(dictionary, anfang, ende):
    count = 0
    for key in range(anfang, ende):
        wort = dictionary[key]
        count = count + vokal_zaehler(wort)
    return count

def vokal_zaehler(wort):
    count_vokale = 0
    for c in list(wort.lower()):
        if c in vokale:
            count_vokale = count_vokale + 1
    return count_vokale

text = "Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appellantur."

text_array = text.replace(',', '').replace('.', '').split()

dictionary = {}

# Füge Wörter in dictionary ein
for count, wort in enumerate(text_array):
    dictionary[count] = wort

# Alternativ: dictionary = dict(enumerate(text_array))

count_letters = 0

for wort in dictionary.values():
    count_letters = count_letters + len(wort)

# Alternativ: count_letters = len(''.join(dictionary.values()))

print(f"Der Text hat {count_letters} Buchstaben")

anzahl_worte = max(dictionary.keys())
print(anzahl_worte)

mitte = anzahl_worte // 2 + 1

vokale_links = vokale_in_woertern(dictionary, 0, mitte)
vokale_rechts = vokale_in_woertern(dictionary, mitte, anzahl_worte)

if vokale_rechts > vokale_links:
    print("Rechts hat mehr Vokale")
elif vokale_links > vokale_rechts:
    print("Links hat mehr Vokale")
else:
    print("Alles gleich")