#Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja na osnovu ulazne
# liste čiji su elementi podliste, kreira listu u kojoj svaki element rezultujude liste predstavlja
# podlistu koja je razlika susednih podlisti ulazne liste.
# Primer: kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]) =[[1, 3], [2], [4, 6, 7]]
def kreiraj(lista):
    novaLista = []
    for i in range(len(lista) - 1):
        razlika = [] #ovo mora da bude unutra
        for el in lista[i]:
            if el not in lista[i + 1]:
                razlika.append(el)
        novaLista.append(razlika)
    print(novaLista)

kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]])
