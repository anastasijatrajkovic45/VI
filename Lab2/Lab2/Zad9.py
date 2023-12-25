# Korišdenjem programskog jezika Python, napisati funkciju zamena, koja u listi brojeva, brojeve manje od broja x,
# koji se prosleđuje kao argument, zamenjuje zbirom svih vrednosti ulazne liste, koje imaju indeks vedi od indeksa
# broja koji se obrađuje. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: zamena([1, 7, 5, 4, 9, 1, 2, 7], 5) = [35, 7, 5, 19, 9, 9, 7, 7]
def zamena(lista, x):
    lista = [sum(lista[i+1:]) if lista[i] < x else lista[i] for i in range(len(lista))]
    print(lista)

zamena([1, 7, 5, 4, 9, 1, 2, 7], 5)

