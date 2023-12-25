# Korišdenjem programskog jezika Python, napisati funkciju objedini, koja od liste tuple objekata kreira dictionary.
# Prvi element svakog tuple objekta postaje ključ rečnika, dok sve ostale vrednosti postaju vrednost (lista vrednosti).
# Ukoliko tuple podatak ima manje od 2 vrednosti, na mesto vrednosti postaviti None. Ukoliko ključ ved postoji u rečniku,
# prepisati njegovu vrednost novom. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]) = { 1: [4, 5], 3: [4, 5], 7: None, 6: [2, 1, 3] }
def objedini(lista):
    rezultat={t[0]:list(t[1:]) if len(t)>0 else None for t in lista}
    print(rezultat)

objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)])