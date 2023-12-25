#Korišdenjem programskog jezika Python, napisati funkciju prosek, koja za svaki element
#prosleđene liste, koja se sastoji isključivo od podlisti, vrada aritmetičku sredinu svih njenih vrednosti.
#Primer: prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]) =[3.25, 4.75, 4.0, 5.0]
def prosek(lista):
    s=0
    novaLista=[]
    for el in lista:
        if isinstance(el, list):
            s=sum(el)/len(el)
        novaLista.append(s)
    print(novaLista)

prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]])
