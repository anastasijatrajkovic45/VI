#Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja računa vrednost elementa u rezultujudem
# nizu korišdenjem 3 uzastopna elementa u nizu koji je prosleđen, korišdenjem funkcije koja se takođe prosleđuje kao
# parametar. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z) = [7, 11, 43]
def izracunaj(niz, funkcija):
    rezultat = [funkcija(niz[i], niz[i+1], niz[i+2]) for i in range(len(niz)-2)]
    print(rezultat)

izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z)

