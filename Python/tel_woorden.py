from statistics import mean
from collections import Counter

# tel de woorden in een zin
woorden = "Dit is een zin die nergens op slaat, en die ook nog een fout is".split()
lengtes = []
for woord in woorden:
    lengtes.append(len(woord))
gemiddelde_lengte = mean(lengtes)
print("jouw zin: ", woorden)
print("gemiddelde lengte van de woorden: ", round(gemiddelde_lengte, 1))
print("lengte van het kortste woord: ", min(lengtes))
print("lengte van het langste woord: ", max(lengtes))

# hoeveel woorden zijn er met de letter e
aantal_komma = 0
for woord in woorden:
    if ',' in woord:
        aantal_komma += 1
print("aantal komma's in de zin: ", aantal_komma)

# wat is de meest voorkomende letter in de zin (letterfrequentie)

def meest_voorkomende_letter(woorden):
    letters = ''.join(woorden).replace(' ', '') # verwijder spaties
    print(letters)
    counter = Counter(letters) # tel de frequentie van elke letter
    print(counter)
    # haal de meest voorkomende letter op
    meest_voorkomende = counter.most_common(1)[0]
    # return de letter en het aantal keer dat deze voorkomt
    meest_voorkomende = (meest_voorkomende[0], meest_voorkomende[1])
    # return de meest voorkomende letter en het aantal keer dat deze voorkomt
    if meest_voorkomende[0] == ',':
        meest_voorkomende = ('geen letter', 0)  # als de meest voorkomende letter een komma is, return dan geen letter
    else:
        meest_voorkomende = (meest_voorkomende[0], meest_voorkomende[1])  # anders return de letter en het aantal keer dat deze voorkomt
    return meest_voorkomende
meest_voorkomende = meest_voorkomende_letter(woorden)
print("De meest voorkomende letter: ", meest_voorkomende[0], "aantal keer: ", meest_voorkomende[1])

# Maak andere woorden met deze tetters
def andere_woorden(letters):
    from itertools import permutations
    # haal alle mogelijke combinaties van de letters
    combinaties = set([''.join(p) for i in range(1, len(letters) + 1) for p in permutations(letters, i)])
    # filter de combinaties die geen woorden zijn
    woorden = [woord for woord in combinaties if len(woord) > 1]  # filter op lengte > 1
    return woorden
andere_woorden_resultaat = andere_woorden(meest_voorkomende[0])
print("Andere woorden die je kunt maken met de letters van de meest voorkomende letter: ")
print(andere_woorden_resultaat)
for woord in andere_woorden_resultaat:
    print(woord)
# tel de woorden die beginnen met een klinker
def tel_klinkers(woorden):
    klinkers = 'aeiou'
    aantal = 0
    for woord in woorden:
        if woord[0].lower() in klinkers:  # controleer of de eerste letter een klinker is
            aantal += 1
    return aantal
aantal_klinkers = tel_klinkers(woorden)
print("Aantal woorden die beginnen met een klinker: ", aantal_klinkers)
# tel de woorden die eindigen met een klinker
def tel_klinkers_einde(woorden):
    klinkers = 'aeiou'  
    aantal = 0
    for woord in woorden:
        if woord[-1].lower() in klinkers:  # controleer of de laatste letter een klinker is
            aantal += 1
    return aantal
aantal_klinkers_einde = tel_klinkers_einde(woorden)
print("Aantal woorden die eindigen met een klinker: ", aantal_klinkers_einde)

