def spoji(lista1, lista2):
    if len(lista1)>len(lista2):
        lista2=lista2+[1]*(len(lista1)-len(lista2))
    else:
        lista1=lista1+[1]*(len(lista2)-len(lista1))

    lista=[(a,b,a*b) for a,b in zip(lista1, lista2)]

    return lista

lista1=[1,7,2,4]
lista2=[2,5,2]
print(spoji(lista1,lista2))