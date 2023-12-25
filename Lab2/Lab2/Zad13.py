# Korišdenjem programskog jezika Python, napisati funkciju skupi, koja kreira novu listu tako da svaka dva susedna
# elementa liste ciji su elementi iskljucivo podliste zamenjuje podlistom koja sadrži zbir elemeata na
# odgovarajudim pozicijama. Elemente koji nedostaju tretirati kao nule.
# Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: skupi([[1, 3, 5], [2, 4, 6], [1, 2]]) = [[3, 7, 11], [3, 6, 6]]
def skupi(lista):
    rezultat=[[a + b for a, b in zip(x, y)] for x, y in zip(lista, lista[1:])]
    print(rezultat)

skupi([[1, 3, 5], [2, 4, 6], [1, 2]])




