# Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja broji koliko karaktera se ponavlja
# uzastopno više puta u prosleđenom stringu.  Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: izbaci("aatesttovi") = 2
def brojanje(tekst):
    s = sum([1 for i in range(len(tekst)-1) if tekst[i] == tekst[i+1]])
    print(s)

brojanje("aatesttovi")

