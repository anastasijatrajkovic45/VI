# Korišdenjem programskog jezika Python, napisati funkciju brojevi, koja iz stringa izvlači listu svih brojeva koji se
# u njemu nalaze. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: brojevi("42+10=52;10*10=100") = [ 42, 10, 52, 10, 10, 100 ]
def brojevi(tekst):
    rezultat =  [int(x) for x in tekst.replace('+', ' ').replace('=', ' ').replace(';', ' ').replace('*', ' ').split() if x.isdigit()]
    print(rezultat)

brojevi("42+10=52;10*10=100")
