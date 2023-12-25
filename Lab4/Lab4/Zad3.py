def pogodi_broj(tajni_broj):
    pogodjene_pozicije = {}

    def proveri_pozicije(cifra):
        pozicije = [i for i, d in enumerate(tajni_broj) if d == cifra]
        return pozicije

    #jos koliko praznih pozicija je ostalo, nije pogodjeno
    def heuristika(cifra):
        pozicije = proveri_pozicije(cifra)
        return len(set(pozicije) - set(sum(pogodjene_pozicije.values(), [])))

    redosled_cifara = []
    stanja = []
    for _ in range(12):
        najbolja_cifra = None
        najbolja_vrednost = -1

        for pozicija in range(10):
            if str(pozicija) not in pogodjene_pozicije:
                vrednost = heuristika(str(pozicija))
                if vrednost > najbolja_vrednost:
                    najbolja_cifra = str(pozicija)
                    najbolja_vrednost = vrednost

        pogodjene_pozicije[najbolja_cifra] = proveri_pozicije(najbolja_cifra)
        redosled_cifara.append(najbolja_cifra)

        if len(pogodjene_pozicije) == 10:
            break

        # cuvanje trenutnog stanja
        trenutno_stanje = {
            'Pogodjene pozicije': pogodjene_pozicije.copy(),
            'Redosled cifara': redosled_cifara.copy()
        }
        stanja.append(trenutno_stanje)
    return stanja

tajni_broj = "271804853428"
sva_stanja = pogodi_broj(tajni_broj)

# Ispis svih stanja
for i, stanje in enumerate(sva_stanja):
    print(f"Korak {i + 1}:")
    print("Pogodjene pozicije:", stanje['Pogodjene pozicije'])
    print("Redosled pogodjenih cifara:", stanje['Redosled cifara'])
    print()
