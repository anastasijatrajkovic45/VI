# Korišdenjem programskog jezika Python, napisati funkciju tekst, koja karaktere u tekstu koji su van opsega malih,
# velikih slova i cifara (65-90 velika i 97-122 mala slova, 48-57 cifre), zamenjuje unicode vrednošdu \ubbbb,
# gde bbbb predstavlja četvorocifrenu unicode reprezentaciju slova koje se menja. Zabranjeno je korišdenje petlji
# (osim u comprehension sintaksi). Napomena: Za preuzimanje unicode reprezentacije slova mogude je koristiti funkciju ord,
# dok se za upisivanje određenog broja nula ispred broja koristi funkcija zfill(brojNula). Prevođenje broja iz dekadnog u
# heksadekadni se vrši korišdenjem funkcije hex. \
#     Primer: tekst("Otpornost 10Ω.") = 'Otpornost\\u002010\\u03A9\\u002E'
def tekst(ulazni_tekst):
    rez= ''.join([c if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57 else '\\u' + hex(ord(c))[2:].zfill(4) for c in ulazni_tekst])
    print(rez)

tekst("Otpornost 10Ω.")

