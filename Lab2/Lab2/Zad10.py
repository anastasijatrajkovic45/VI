# Korišdenjem programskog jezika Python, napisati funkciju stepen, koja svaki par dva broja u ulaznoj listi (x, y),
# transformiše u xy. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]) = [1, 25, 64, 6, 1, 216, 9, 512]
from itertools import starmap
def stepen(lista):
    lista=[lista[i]**lista[i+1] for i in range(len(lista)-1)]
    print(lista)

stepen([1, 5, 2, 6, 1, 6, 3, 2, 9])