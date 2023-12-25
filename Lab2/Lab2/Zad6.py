# Korišdenjem programskog jezika Python, napisati funkciju objedini, koja 2 liste brojeva objedinjuje u jednu listu
# koja se sastoji od parova brojeva (tuple). Dužina liste treba da je dimenzija duže od dve ulazne liste.
# N-ti tuple podatak rezultujude kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe manji,
# a na drugoj vedi broj iz obe liste. Kradu ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste.
# Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: objedini([1, 7, 2, 4, 5], [2, 5, 2]) = [(1, 2), (5, 7), (2, 2), (0, 4), (0, 5)]
def objedini(lista1, lista2):
    lista1 += [0] * (max(len(lista1), len(lista2)) - len(lista1))
    lista2 += [0] * (max(len(lista1), len(lista2)) - len(lista2))
    rezultat=[(min(x,y), max(x,y)) for x,y in zip(lista1,lista2)]
    print(rezultat)

objedini([1, 7, 2, 4, 5], [2, 5, 2])