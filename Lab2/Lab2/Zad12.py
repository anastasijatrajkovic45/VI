# Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja u listi koja se sastoji od brojeva
# i podlisti, menja svaki broj njegovim kvadratom, dok listu zamenjuje zbirom kvadrata brojeva koji je čine.
# Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) = [4, 16, 14, 20, 4, 106]

from functools import reduce
def izracunaj(lista):
    rezultat = [reduce(lambda x, y: x ** 2 + y ** 2, podlista) if isinstance(podlista, list) else podlista ** 2 for
                podlista in lista]
    print(rezultat)


izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]])

