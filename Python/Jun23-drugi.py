def validna_kombinacija(dimenzija, kvadrat=None):
    # Funkcija za proveru jednakosti suma u vrstama, kolonama i dijagonalama
    def proveri_sume(matrica):
        suma_dijagonala1 = sum(matrica[i][i] for i in range(dimenzija))
        suma_dijagonala2 = sum(matrica[i][dimenzija - i - 1] for i in range(dimenzija))

        return all(
            sum(red) == suma_dijagonala1 == suma_dijagonala2
            for red in matrica + list(zip(*matrica))
        )

    # Rekurzivna funkcija za popunjavanje kvadrata
    def popuni_kvadrat(i, j):
        if i == dimenzija:
            return proveri_sume(kvadrat)

        for broj in range(1, dimenzija ** 2 + 1):
            if broj not in set(kvadrat[i] + [kvadrat[x][j] for x in range(i)]):
                kvadrat[i][j] = broj
                novi_j = (j + 1) % dimenzija
                novi_i = i + 1 if novi_j == 0 else i
                if popuni_kvadrat(novi_i, novi_j):
                    return True

        return False

    # Inicijalizujemo kvadrat ako nije prosleđen
    if kvadrat is None:
        kvadrat = [[0] * dimenzija for _ in range(dimenzija)]

    # Pozivamo rekurzivnu funkciju
    if popuni_kvadrat(0, 0):
        return kvadrat
    else:
        return None

# Primer
dimenzija_kvadrata = 3
rezultat = validna_kombinacija(dimenzija_kvadrata)
if rezultat:
    for red in rezultat:
        print(red)
else:
    print("Nema validne kombinacije.")
