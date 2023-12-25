# Korišdenjem programskog jezika Python, napisati funkciju proizvod, koja računa proizvod liste podlisti (A) i
# liste brojeva (B). Smatrati da je broj podlisti u listi A jednak dužini liste B. Funkcija vrada listu koja ima
# onoliko elemenata koliko je dužina ulaznih listi. N-ti element izlazne liste predstavlja sumu svih elemenata
# N-te podliste liste A koji u prethodno pomnoženi N-tim elementom u liste B. Zabranjeno je korišdenje petlji
# (osim u comprehension sintaksi) i funkcije sum. \
#     Primer: proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]) = [6, 30, 72]
def proizvod(A, B):
    rezultat = [sum(x * B[i] for x in podlista) for i, podlista in enumerate(A)]
    print(rezultat)

rezultat = proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3])



