#Korišdenjem programskog jezika Python, napisati funkciju izmeni, koja svaki n-ti element
#liste zamenjuje brojem koji predstavlja sumu svih elemenata originalne liste, od prvog, do
#n-tog elementa.
#Primer: izmeni([1, 2, 4, 7, 9]) = [1, 3, 7, 14, 23]

def izmeni(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
        lista[i]=s
    print(lista)

izmeni([1, 2, 4, 7, 9])
