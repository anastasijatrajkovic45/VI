#Korišdenjem programskog jezika Python, napisati funkciju izbroj, koja određuje broj
# elemenata liste, gde svaki element može da bude podlista ili broj.
# Primer: izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) = 13
def izbroj(lista):
    broj=0
    for el in lista:
        if isinstance(el, list):
            broj+= izbroj(el)
        else:
            broj+=1
    return broj

rezultat=izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6])
print(rezultat)