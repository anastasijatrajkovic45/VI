from itertools import combinations

def generiraj_tuplove(ulazni_string):
    brojevi = [int(c) for c in ulazni_string]  
    tuplovi = [(max(broj1, broj2), min(broj1, broj2), abs(broj1 - broj2)) 
               for broj1, broj2 in combinations(brojevi, 2)]
    return tuplovi

ulazni_string = "1536"
rezultat = generiraj_tuplove(ulazni_string)
print(rezultat)
