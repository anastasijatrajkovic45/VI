def bezbedno(tabla, x, y):
    # provera horizontalno
    for i in range(y):
        if tabla[x][i] == 1:
            return False

    # provera gornje dijagonale
    i, j = x, y
    while i >= 0 and j >= 0:
        if tabla[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # provera donje dijagonale
    i, j = x, y
    while i < len(tabla) and j >= 0:
        if tabla[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def degree_heuristika(tabla, kolona):
    broj_slobodnih_polja = {}
    for j in range(len(tabla)):
        broj_slobodnih_polja[j] = sum(1 for i in range(len(tabla[j])) if tabla[j][i] == 0)

    #sortiranje kolona prema broju slobodnih polja
    sortirane_kolone = sorted(range(len(tabla)), key=lambda k: broj_slobodnih_polja[k])
    return sortirane_kolone

def forward_checking(tabla, red, kolona):
    for i in range(len(tabla)):
        if tabla[i][kolona] == 0 and i != red:
            tabla[i][kolona] = -1

    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if (i == red or j == kolona or abs(i - red) == abs(j - kolona)) and tabla[i][j] == 0:
                tabla[i][j] = -1
def dfs_rasporedi_kraljice(tabla, kolona=0):
    if kolona == len(tabla):
        return True

    sortirane_kolone = degree_heuristika(tabla, kolona)

    for red in sortirane_kolone:
        if bezbedno(tabla, red, kolona):
            tabla[red][kolona] = 1
            forward_checking(tabla, red, kolona)

            if dfs_rasporedi_kraljice(tabla, kolona + 1):
                return True

            # backtracking ako se ne moze postaviti kraljica u sledecu kolonu
            tabla[red][kolona] = 0
            for i in range(len(tabla)):
                for j in range(len(tabla)):
                    if tabla[i][j] == -1:
                        tabla[i][j] = 0
    return False
def ispisi_tablu(tabla):
    for red in tabla:
        print(red)

tabla = [[0 for _ in range(8)] for _ in range(8)]
dfs_rasporedi_kraljice(tabla)
ispisi_tablu(tabla)
