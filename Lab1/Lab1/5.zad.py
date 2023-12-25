#Korišdenjem programskog jezika Python, napisati funkciju brojel, koja broji koliko
# elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko elemenat liste nije
# podlista funkcija vrada -1.
# Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]
def brojel(lista):
    for el in lista:
        if isinstance(el,list):
            lista=len(el)
        elif isinstance(el, str):
            lista=-1
        print(lista)

brojel([[1, 2], [3, 4, 5], 'el', ['1', 1]])

