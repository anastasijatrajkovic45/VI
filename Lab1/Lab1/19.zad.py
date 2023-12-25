#Korišdenjem programskog jezika Python, napisati funkciju stepenuj, koja listu tuple
# vrednosti transformiše u listu brojeva, koji se dobijaju primenom operacije stepenovanja,
# tako što se prvi element stepenuje drugim, zatim se rezultat stepenuje tredim sve dok se
# ne dođe do poslednjeg elementa u tuple-u.
# Primer: stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]) = [1, 32, 256, 5]
def stepenuj(lista):
    novaLista = []
    for el in lista:
        rez = el[0]
        for i in range(len(el)-1 ):  # Promenili smo početnu vrednost i granice petlje
            rez **= el[i]
        novaLista.append(rez)
    print(novaLista)

stepenuj([(1, 4, 2), (2, 3, 1), (2, 2, 2, 2), (5, )])




