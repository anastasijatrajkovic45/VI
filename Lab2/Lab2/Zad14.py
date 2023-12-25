# Korišdenjem programskog jezika Python, napisati funkciju suma, koja prvenstveno određuje proizvod elemenata u
# svakoj podlisti unutar prosleđene liste, a zatim sumu tako dobijenih elemenata. Zabranjeno je korišdenje petlji
# (osim u comprehension sintaksi) i funkcije sum i prod.
# Primer: suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = 630
from functools import reduce
def suma(lista):
    rez2=0
    for el in lista:
        rez1=reduce(lambda x,y:x*y,el )
        rez2+=rez1
    print(rez2)
suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])