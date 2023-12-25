# Korišdenjem programskog jezika Python, napisati funkciju poredak, koja 2 liste brojeva objedinjuje u jednu listu
# koja se sastoji od tuple objekata koji imaju tri elementa. Prvi element rezultujude kolekcije je element prve liste,
# drugi je element druge liste a tredi ma vredost ’Jeste’ ukoliko je element druge liste dva puta vedi od elementa
# prve liste, odnosno ‘Nije’ ukoliko nije. Dužina liste je dimenzija duže od dve ulazne liste. Kradu ulaznu listu
# dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: poredak ([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 'Jeste'), (7, 5, 'Nije'),  (2, 2, 'Nije'), (4, 0, 'Nije')]
def poredak(lista1, lista2):
    lista1 += [0] * (max(len(lista1), len(lista2)) - len(lista1))
    lista2 += [0] * (max(len(lista1), len(lista2)) - len(lista2))

    rezultat = [(x, y, 'Jeste' if y > 2 * x else 'Nije') for x, y in zip(lista1, lista2)]
    print(rezultat)

poredak([1, 7, 2, 4], [2, 5, 2])

