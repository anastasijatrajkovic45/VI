def kreiraj(lista):
    recnik={x[0]: sum(x[1:]) for x in lista}
    return recnik

lista=[(1,), (3,4,5), (7,), (1,4,5), (6,2,1,3)]
print(kreiraj(lista))