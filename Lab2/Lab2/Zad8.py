# Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja u listi koja može da se sastoji od brojeva
# i podlisti, na n-tom mestu u rezultujudem nizu upisuje broj sa n-te pozicije iz ulaznog niza, a ukoliko se radi o podlisti,
# zamenjuje je proizvodom svih brojeva u podlisti. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]) = [1, 5, 15, 8, 2, 18]
from functools import reduce
from functools import reduce
def izracunaj(lista):
    rezultat = [reduce((lambda x, y: x * y), el) if isinstance(el, list) else el for el in lista]
    print(rezultat)

izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]])

# def izracunaj(lista):
#     rezultat=[]
#     for el in lista:
#         if isinstance(el,list):
#             proizvod=reduce((lambda x, y: x * y), el)
#             rezultat.append(proizvod)
#         else:
#             rezultat.append(el)
#     print((rezultat))
#
# izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]])