def maxTuple(lista1, lista2):
    tuple_lista=[[e1,e2] for e1,e2 in zip(lista1,lista2)]
    kombinovana_lista=[[[a,b] for a,b in zip(*t)] for t in tuple_lista]
    print(kombinovana_lista)
    max_pair=max(kombinovana_lista, key=lambda x: x[1])
    maks=max(max_pair, key=lambda x: x[1])
    return maks

# Primer
lista1 = [[1, 2], [3, 4], [5, 6]]
lista2 = [[7, 0], [5, 8], [9, 3]]

rezultat = maxTuple(lista1, lista2)
print(rezultat)
