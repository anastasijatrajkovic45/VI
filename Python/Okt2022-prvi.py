def uredi(lista1, lista2):
    if len(lista1)>len(lista2):
        lista2=lista2+[0]*abs(len(lista1)-len(lista2))
    else:
        lista1=lista1+[0]*abs(len(lista1)-len(lista2))

    lista=[(a,b, 'Da' if a>b else 'Ne') for a,b in zip(lista1,lista2) ]

    return lista

lista1=[1,6,2,5]
lista2=[2,3,3]
print(uredi(lista1, lista2))


