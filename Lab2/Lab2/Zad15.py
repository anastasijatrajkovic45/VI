# Korišdenjem programskog jezika Python, napisati funkciju promeni, koja u listi brojeva, brojeve vede ili
# jednake broju x, koji se prosleđuje kao argument, umanjuje za x, dok brojeve manje od x uvedava za x.
# Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: promeni([7, 1, 3, 5, 6, 2], 3) = [4, 4, 0, 2, 3, 5]
def promeni(lista, x):
    rezultat= [broj - x if broj >= x else broj + x for broj in lista]
    print(rezultat)

promeni([7, 1, 3, 5, 6, 2], 3)

