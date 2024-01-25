def transformacija(lista1, lista2):
    kombinovana_lista=[]
    if (len(lista1)>len(lista2)):
        lista2=lista2 + [0]*(len(lista1)-len(lista2))
    else:
        lista1=lista1+[0]*(len(lista2)-len(lista1))

    kombinovana_lista=[[a,b] for a, b in zip(lista1, lista2)]


    # for el in kombinovana_lista:
    #     kljuc=f"{el[0]} - {el[1]}"
    #     recnik[kljuc]='jeste' if el[0]>el[1] else 'nije'

    recnik=dict(map(lambda el:(f'{el[0]}-{el[1]}', 'jeste' if el[0]>el[1]else 'nije'), kombinovana_lista))


    return recnik

lista1=[2,10,6,8]
lista2=[1,5,9]
print(transformacija(lista1,lista2))



