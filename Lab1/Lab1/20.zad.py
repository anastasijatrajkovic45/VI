#Korišdenjem programskog jezika Python, napisati funkciju boje, koja RGB heksadekadni
# zapis boje deli po kanalima i vrada rečnik sa odgovarajudim vrednostima u dekadnom formatu.
# Napomena: int("Broj u bazi N", N) može da se koristi za prevođenje iz baze N u bazu 10.
# Primer: boje("#FA1AA0") = { "Red": 250, "Green": 26, "Blue": 160 }
def boje(heks_boja):

    if heks_boja.startswith("#"): #uklanja se #
        heks_boja = heks_boja[1:]

    crvena = heks_boja[0:2]
    zelena = heks_boja[2:4]
    plava = heks_boja[4:6]

    red_vrednost = int(crvena, 16)
    green_vrednost = int(zelena, 16)
    blue_vrednost = int(plava, 16)

    rezultat = {"Red": red_vrednost, "Green": green_vrednost,"Blue": blue_vrednost}
    print(rezultat)

boje("#FA1AA0")

