# Korišdenjem programskog jezika Python, napisati funkciju suma, koja vrada sumu svih elemenata u listi brojeva i
# svim njenim podlistama. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi) i funkcije sum. \
# Primer: suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = 45
def suma(lista):
    s=0
    for podlista in lista:
        for i in range(len(podlista)):
            s+=podlista[i]
    print(s)

suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])