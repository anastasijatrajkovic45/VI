#Korišdenjem programskog jezika Python, napisati funkciju unija, koja prihvata dve liste
# (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
# elemenata obe liste bez ponavljanja.
# Primer: unija([5, 4, "1", "8", 7], [1, 9, "1"]) = [5, 4, "1", "8", 7, 9, 1]
def unija(lista1, lista2):
    rezultat=[]
    skup1=set(lista1)
    skup2=set(lista2)
    rezultat=list(skup1.union(skup2))
    return rezultat

lista=[]
lista=unija([5, 4, "1", "8", 7], [1, 9, "1"])
print(lista)