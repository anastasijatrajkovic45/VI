#Korišdenjem programskog jezika Python, napisati funkciju saberi, koja listu tuple vrednosti
# transformiše u listu brojeva, koji se dobijaju primenom operacije sabiranja.
# Primer: operacija([(1, 4, 6), (2, 4), (4, 1)]) = [11, 6, 5]
def saberi(lista):
    novaLista=[]
    for el in lista:
        if isinstance(el, tuple):
            novaLista.append(sum(el))
    print(novaLista)

saberi([(1, 4, 6), (2, 4), (4, 1)])