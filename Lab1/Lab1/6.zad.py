#Korišdenjem programskog jezika Python, napisati funkciju razlika, koja prihvata dve liste
# (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svi
# elemenata iz prve liste, koji se ne nalaze u drugoj listi.
# Primer: razlika([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"]
def razlika(lista1, lista2):
    novaLista=[]
    for el in lista1:
        if el not in lista2:
            novaLista.append(el)
    print(novaLista)


razlika([1, 4, 6, "2", "6"], [4, 5, "2"])

