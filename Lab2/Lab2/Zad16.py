#Korišdenjem programskog jezika Python, napisati funkciju broj, koja na osnovu heksadekadnog broja koji predstavlja boju
# na ulazu u formatu #RGB, određuje integer reprezentaciju tog broja, koja se dobija slededim obrascem:
# (R * 65536) + (G * 256) + B. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Napomena: Broj N je mogude prevesti iz baze B u bazu 10 korišdenjem funkcije int(N, B)
# Primer: broj("#FA0EA0") = 16387744
def broj(boja):
    rez=int(boja[1:3], 16) * 65536 + int(boja[3:5], 16) * 256 + int(boja[5:], 16)
    print(rez)

broj("#FA0EA0")
