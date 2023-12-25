#Korišdenjem programskog jezika Python, napisati funkciju parni, koja listu brojeva
#transformiše u rečnik parnih i neparnih brojeva.
#Primer: parni([1, 7, 2, 4, 5]) = {'Parni': [2, 4], 'Neparni': [1, 7, 5]}
def parni(lista):
    parni_brojevi = []
    neparni_brojevi = []

    for el in lista:
        if el%2==0:
            parni_brojevi.append(el)
        else:
            neparni_brojevi.append(el)
        rezultat={'Parni': parni_brojevi, 'Neparni': neparni_brojevi}
    return rezultat

rez=parni([1, 7, 2, 4, 5])
print(rez)