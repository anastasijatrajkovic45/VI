#Korišdenjem programskog jezika Python, napisati funkciju numlista, koja iz liste koja može
#da sadrži elemente različitog tipa izdvaja vrednosti po tipu i smešta ih u rečnik.
# Napomena: Naziv tipa može da se preuzme korišćenjem atributa __name__ nad samim tipom podataka.
# Primer: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) ={'str': ["Prvi", "Drugi"], 'int': [2, 4], 'list': [[3, 5]]}
def numlista(lista):
    strList=[]
    intList=[]
    listList=[]
    for el in lista:
        if type(el)==int:
            intList.append(el)
        elif type(el)==list:
            listList.append(el)
        else:
            strList.append(el)
        rezultat={'str':strList, 'int':intList, 'list':listList}#recnik!
    return  rezultat

rez=numlista(["Prvi", "Drugi", 2, 4, [3, 5]])
print(rez)