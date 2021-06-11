
woerter = {
  'Antriebsritzel':   'drive pinion',
  'Biegeeigenschaft': 'bending property',
  'Drehklappe':       'butterfly valve',
  'Istspiel':         'actual clearance',
  'Keilriemen':       'V-belt',
}

def de_en(wort):
    if wort in woerter:
        return woerter[wort]
    else:
        return "<unbekanntes Wort>"

if __name__ == '__main__':
    print(de_en('Keilriemen'))
    print(de_en('butterfly valve'))
