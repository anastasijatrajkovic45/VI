#Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja na osnovu datog
# rečnika koji sadrži elemente različitog tipa kreira listu tuple objekata. Svaki tuple objekat
# na prvoj poziciji sadrži tip elementa a na drugoj koliko je takvih elemenata bilo u rečniku.
# Primer: brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}) =[('int', 3), ('list', 2), ('str',1)]
def brojanje(recnik): #sam prepoznaje da je recnik!
    nizInt=[]
    nizList=[]
    nizStr=[]
    vrednosti=recnik.values()
    for el in vrednosti:
        if isinstance(el, int):
            nizInt.append(el)
        elif isinstance(el, list):
            nizList.append(el)
        else:
            nizStr.append(el)
    brojStr=len(nizStr)
    brojList=len(nizList)
    brojInt=len(nizInt)
    rezultat=[('int', brojInt), ('list', brojList),('str', brojStr)]
    print(rezultat)

brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8})