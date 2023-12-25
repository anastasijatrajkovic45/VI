# Korišdenjem programskog jezika Python, napisati funkciju spoji, koja 2 liste brojeva objedinjuje u jednu listu
# koja se sastoji od tuple objekata koji imaju tri elementa. Prvi element rezultujude kolekcije je element prve liste,
# drugi je element druge liste a tredi je zbir elemenata. Dužina liste je dimenzija duže od dve ulazne liste.
# Nti tuple podatak rezultujude kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe manji,
# a na drugoj vedi broj iz obe liste. Kradu ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste.
# Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: spoji([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 3), (5, 7, 12), (2, 2, 4), (0, 4, 4)]
def spoji(lista1, lista2):
    lista1 += [0] * (max(len(lista1), len(lista2)) - len(lista1))
    lista2 += [0] * (max(len(lista1), len(lista2)) - len(lista2))

    rezultat = [(min(x,y), max(x,y), x+y ) for x, y in zip(lista1, lista2)]
    print(rezultat)

spoji([1, 7, 2, 4], [2, 5, 2])