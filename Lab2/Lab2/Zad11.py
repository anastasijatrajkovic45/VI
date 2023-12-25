# Korišdenjem programskog jezika Python, napisati funkciju proizvod, koja vrada proizvod svih elemenata u listi brojeva
# i svim njenim podlistama. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi) i funkcije prod. \
#     Primer: proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]]) = 4320
from functools import reduce
def proizvod(lista):
    rezultat = reduce(lambda x, y: x * reduce(lambda a, b: a * b, y), lista, 1)
    print(rezultat)

proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]])