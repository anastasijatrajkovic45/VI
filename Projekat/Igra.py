from copy import deepcopy
from functools import cache, reduce
import heapq
import math
from Tabla import Tabla
from termcolor import cprint
from collections import deque

class Igra:
    def __init__(self):
        self.dimenzija = 0
        self.igrac = 'X'
        self.brojac_stack_x = 0
        self.brojac_stack_o = 0
        self.potez = ('', -1, -1, '')
        self.stanja = 0
        self.stanjahash = dict()
        self.abhash = dict()
        self.odigrani_potezi = 0

    def izbor_prvog_igraca(self):
        while True:
            izbor = input("Izaberite ko igra prvi - unesite 'racunar' ili 'covek': ").lower()
            if izbor == 'racunar':
                return 'Racunar na potezu'
            elif izbor == 'covek':
                return 'Vi ste na potezu'
            else:
                print ("Molimo unesite 'racunar' ili 'covek'.")

    def postavi_velicinu_table(self):
        self.dimenzija = -1
        while self.dimenzija < 0 or (self.dimenzija % 8 != 0 and self.dimenzija != 10):
            try:
                self.dimenzija = int(input("Unesite dimenziju table (preporučeno 8): "))
                if self.dimenzija % 8 != 0 and self.dimenzija != 10:
                    print("Dimenzija mora biti deljiva sa 8 ili imati dimenziju 10. Pokušajte ponovo.")
            except ValueError:
                print("Nije validna vrednost. Pokušajte ponovo.")
        self.tabla = Tabla(self.dimenzija)
        print(f"Dimenzija table je {self.dimenzija}, a velicina table je {self.dimenzija}x{self.dimenzija}")

    def crtaj_tablu(self):
        self.tabla.iscrtaj_tablu()
    
    def postavi_igraca(self):
        while True:
            self.igrac = input("Izaberite igraca (X ili O): ")
            if self.igrac.upper() == 'X':
                return 'X'
            elif self.igrac.upper() == 'O':
                return 'O'
            else:
                print("Pogrešan unos. Molimo vas izaberite X ili O.")

    def unos_poteza(self):
        potez = ('', -1, -1, '')
        uspesno = False
        while not uspesno:
            r = ('', -1, -1, '')
            try:
                unos = str.split(input("Unesi potez u obliku \"VRSTA KOLONA MESTO SMER\": "))
                if len(unos)==4 and unos[0].isalpha() and unos[1].isdigit() and 0 <= int(unos[2]) <= 7:
                    r = (unos[0].upper(), int(unos[1]), int(unos[2]), unos[3])
                else:
                    print("Nevalidan unos za vrstu, kolonu, mesto ili smer.")
                    continue
                potez = r
            except:
                print("Nevalidan unos")
                continue

            if self.ispravnost_poteza(potez):
                    uspesno = True
            return potez
    
    def ispravnost_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez
        if kolona < 0 or kolona > self.dimenzija or vrsta<'A' or vrsta > chr(ord('A') + self.dimenzija - 1) or smer not in ['GD', 'GL', 'DD', 'DL']:
            print("Uneli ste pogresnu vrstu, kolonu ili smer.")
        else:
            indeks_vrste = ord(vrsta) - ord('A')
            indeks_kolone = kolona - 1
            mesto-=1
            red_poz, kol_poz = 2 - (mesto // 3), mesto % 3
            matrica_3x3 = self.tabla.matrica[indeks_vrste][indeks_kolone]
            
            for _ in range(2,-1,-1):
                for _ in range(0,3):
                    if matrica_3x3[red_poz][kol_poz]==self.igrac:
                        return True
                    else:
                        print("Na tom mestu se ne nalazi vasa figura.")
                        return False
                
    def proveri_kraj_igre(self):
        broj_figura=self.dimenzija/2*(self.dimenzija-2)
        if self.brojac_stack_x >= broj_figura/(2*self.dimenzija) or self.brojac_stack_o >= broj_figura/2*self.dimenzija :
            for i in range(len(self.tabla.matrica)):
                    for j in range(len(self.tabla.matrica[i])):
                        for k in range(len(self.tabla.matrica[i][j])):
                            for l in range(len(self.tabla.matrica[i][j][k])):
                                self.tabla.matrica[i][j][k][l] = '.'
            if self.brojac_stack_x >= broj_figura/2*self.dimenzija:
                print('Pobednik je igrač X!')
                return True
            elif self.brojac_stack_o >= broj_figura/2*self.dimenzija:
                print('Pobednik je igrač O!')
                return True
        elif self.dimenzija==10:
            if self.brojac_stack_o >= (broj_figura/2*self.dimenzija) or self.brojac_stack_x==self.brojac_stack_o:
                print('Nereseno')
                return True
        else:
            print("Igra se nastavlja...") 
            return False

    ### 2.FAZA
    def brojac_figura(self, matrica3x3):
        brojac = 0
        for i in range(2,-1,-1):
            for j in range(0,3):
                figura=matrica3x3[i][j]
                if figura=='X' or figura=='O':
                    brojac+=1
        return brojac
    
    def proveri_stek(self, matrica3x3):
        broj_figura=self.brojac_figura(matrica3x3)
        if broj_figura==8:
            print("Stek je popunjen.")
            if matrica3x3[0][1]=='X':
                self.brojac_stack_x+=1
                print(f"Stek pripada igracu X. On ima {self.brojac_stack_x} steka.")
                for i in range(0,3):
                    for j in range(0,3):
                        matrica3x3[i][j]='.'
            elif matrica3x3[0][1]=='O':
                self.brojac_stack_o+=1
                print(f"Stek pripada igracu O. On ima {self.brojac_stack_o} steka.")
                for i in range(0,3):
                    for j in range(0,3):
                        matrica3x3[i][j]='.'
        return matrica3x3
    
    def smerovi(self, potez):
        vrsta, kolona, mesto, smer = potez
        indeks_vrste, indeks_kolone = ord(vrsta) - ord('A'), kolona - 1

        if smer == 'GD':
            nova_vrsta = indeks_vrste - 1
            nova_kolona = indeks_kolone + 1
        if smer == 'GL':
            nova_vrsta = indeks_vrste - 1
            nova_kolona = indeks_kolone - 1
        if smer == 'DD':
            nova_vrsta = indeks_vrste + 1
            nova_kolona = indeks_kolone + 1
        if smer == 'DL':
            nova_vrsta = indeks_vrste + 1
            nova_kolona = indeks_kolone - 1

        return nova_vrsta, nova_kolona
    
    def pomeri_figure(self, potez):
        vrsta, kolona, mesto, smer = potez
        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = int(kolona) - 1 
        nova_vrsta, nova_kolona=self.smerovi(potez)

        matrica_iz = self.tabla.matrica[indeks_vrste][indeks_kolone]

        if nova_vrsta < 0 or nova_vrsta >= len(self.tabla.matrica) or nova_kolona < 0 or nova_kolona >= len(self.tabla.matrica[0]):
            return None

        matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
        mesto-=1
        red_poz, kol_poz = 2 - (mesto // 3), mesto % 3

        for i in range(red_poz, -1,-1):
                for j in range(kol_poz, 3) if i == 2 - (mesto // 3) else range(0,3):
                    for x in range(2, -1, -1):
                        for y in range(3):
                            if matrica_u[x][y] == '.':
                                element = matrica_iz[i][j]
                                matrica_iz[i][j] = '.'
                                matrica_u[x][y] = element
        
        matrica_u=self.proveri_stek(matrica_u)
        return self.tabla.matrica
    
    def valjanost_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez

        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1
        nova_vrsta, nova_kolona = self.smerovi(potez)

        matrica_iz = self.tabla.matrica[indeks_vrste][indeks_kolone]
        matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
        mesto -= 1
        red_poz, kol_poz = 2 - (mesto // 3), mesto % 3
        
        broj_figura_na = 0
        for i in range(red_poz, -1,-1):
            for j in range(kol_poz, 3) if i == 2 - (mesto // 3) else range(0,3):
                figura=matrica_iz[i][j]
                if figura == 'X' or figura == 'O':
                    broj_figura_na += 1

        broj_figura_u = self.brojac_figura(matrica_u)
        broj_figura_iz = self.brojac_figura(matrica_iz) - broj_figura_na

        if broj_figura_u < broj_figura_iz:
            print("Broj figura u steku na kom se premesta figura ili stek treba da bude veci od broja figure u steku sa kog se pomera figura ili stek.")
            return False
        elif(broj_figura_u + broj_figura_na) > 8:
            print("U steku ne može biti više od osam figura. Pokusajte ponovo.")
            return False
        else:
            if nova_vrsta >= 0 and nova_vrsta < self.dimenzija and nova_kolona >= 0 and nova_kolona < self.dimenzija and indeks_kolone > 0 and indeks_kolone < self.dimenzija-1 :
                matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
                matrica_gl = self.tabla.matrica[indeks_vrste - 1][indeks_kolone - 1]
                matrica_dl = self.tabla.matrica[indeks_vrste + 1][indeks_kolone - 1]
                matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
                matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]

                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gl[i][j] == '.' and matrica_gd[i][j] == '.' and matrica_dl[i][j] == '.' and matrica_dd[i][j] == '.':
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                print("Izaberite smer do najblizeg steka.")
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
                        else:
                            print("Izaberite polje na kome postoji stek.")
                            return False          
                
            if indeks_kolone == self.dimenzija-1: #u poslednjoj koloni, nikako ne diraj
                matrica_gl = self.tabla.matrica[indeks_vrste - 1][indeks_kolone - 1]
                matrica_dl = self.tabla.matrica[indeks_vrste + 1][indeks_kolone - 1]
                validni_smerovi = ['GL', 'DL']
                if smer =='GL':
                    matrica = self.tabla.matrica[indeks_vrste-1][indeks_kolone-1]
                if smer == 'DL':
                    matrica = self.tabla.matrica[indeks_vrste+1][indeks_kolone-1]

                if smer in validni_smerovi:
                    for i in range(2, -1, -1):
                        for j in range(0, 3):
                            if matrica_gl[i][j] == '.' and matrica_dl[i][j] == '.':
                                print("Izaberite polje na kome postoji stek.")
                                return False
                            elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                                return True
                else:
                    print("Ne mozete premestiti figuru u tom smeru.")
                    return False
                            
            if indeks_kolone == 0: # U prvoj koloni, nikako ne diraj
                matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
                matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
                matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]
                validni_smerovi=['GD', 'DD']

                if smer in validni_smerovi:
                    for i in range(2, -1, -1):
                        for j in range(0, 3):
                            if matrica_gd[i][j] == '.' and matrica_dd[i][j] == '.':
                                print("Izaberite polje na kome postoji stek.")
                                return False
                            elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                                return True
                else:
                    print("Ne mozete premestiti figuru u tom smeru.")
                    return False
            else:
                return True
        
    def provera_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez

        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1
        nova_vrsta, nova_kolona=self.smerovi(potez)

        if nova_vrsta >= 0 and nova_vrsta < self.dimenzija and nova_kolona >= 0 and nova_kolona < self.dimenzija and indeks_kolone > 0 and indeks_kolone < self.dimenzija-1 :
            matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
            trenutna_matrica=self.tabla.matrica[indeks_vrste][indeks_kolone]
            matrica_gl = self.tabla.matrica[indeks_vrste - 1][indeks_kolone - 1]
            matrica_dl = self.tabla.matrica[indeks_vrste + 1][indeks_kolone - 1]
            matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
            matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]

            for i in range(2, -1, -1):
                for j in range(0, 3):
                    if matrica_gl[i][j] == '.' and matrica_gd[i][j] == '.' and matrica_dl[i][j] == '.' and matrica_dd[i][j] == '.':
                        if self.priblizava_se_steku(potez):
                            return True
                        else:
                            return False
                    elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                        return True
                    else:
                        return False          
               
        if indeks_kolone == self.dimenzija-1: #u poslednjoj koloni, nikako ne diraj
            matrica_gl = self.tabla.matrica[indeks_vrste - 1][indeks_kolone - 1]
            matrica_dl = self.tabla.matrica[indeks_vrste + 1][indeks_kolone - 1]
            validni_smerovi=['GL', 'DL']
            if smer =='GL':
                matrica = self.tabla.matrica[indeks_vrste-1][indeks_kolone-1]
            if smer == 'DL':
                matrica = self.tabla.matrica[indeks_vrste+1][indeks_kolone-1]

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gl[i][j] == '.' and matrica_dl[i][j] == '.':
                            return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False
                            
        if indeks_kolone == 0:  # U prvoj koloni, nikako ne diraj
            matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
            matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
            matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]
            validni_smerovi=['GD', 'DD']

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gd[i][j] == '.' and matrica_dd[i][j] == '.':
                            return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False

    def da_li_je_stek(self, matrica3x3):
        for i in range(3):
            for j in range(3):
                figura=matrica3x3[i][j]
                if figura=='X' or figura=='O':
                    return True
        return False 
     
    def zauzete_matrice(self, matrica):
        zauzeti_indeksi = {}
        matrica=self.tabla.matrica
        for vrsta_indeks in range(self.dimenzija):
            for kolona_indeks in range(self.dimenzija):
                matrica3x3 = matrica[vrsta_indeks][kolona_indeks]
                if self.da_li_je_stek(matrica3x3):
                    indeks = (vrsta_indeks, kolona_indeks)
                    zauzeti_indeksi[indeks]=8*vrsta_indeks+kolona_indeks+1
        return zauzeti_indeksi
    
    def udaljenost_euklidska(self, potez1, potez2):
        vrsta1, kolona1, mesto, smer = potez1
        vrsta2, kolona2, mesto, smer = potez2

        indeks_vrste1, indeks_kolone1 = ord(vrsta1) - ord('A'), kolona1 - 1
        indeks_vrste2, indeks_kolone2 = ord(vrsta2) - ord('A'), kolona2 - 1

        udaljenost = ((indeks_vrste1 - indeks_vrste2) ** 2 + (indeks_kolone1 - indeks_kolone2) ** 2) ** 0.5
        return udaljenost

    def udaljenosti_izmedju_figura(self, figure):
        figure = []

        for i in range(len(self.tabla.matrica)):
            for j in range(len(self.tabla.matrica[i])):
                polje = self.tabla.matrica[i][j]
                for m in range(len(polje)):
                    for n in range(len(polje[m])):
                        if polje[m][n] == 'X' or polje[m][n] == 'O':
                            figura = (chr(i + ord('A')), j + 1, 3 * (2 - m) + n + 1, '')
                            figure.append(figura)
        udaljenosti = {}
        for i in range(len(figure)):
            for j in range(i + 1, len(figure)):
                figura1 = figure[i]
                figura2 = figure[j]
                udaljenost = self.udaljenost_euklidska(figura1, figura2)
                kljuc = (figura1, figura2)
                udaljenosti[kljuc] = udaljenost
        return udaljenosti
    
    #potrebno za heuristiku
    #svi potezi jednog igraca
    def svi_potezi_igraca(self, igrac):
        svi_potezi, smerovi = [], ['GD', 'GL', 'DD', 'DL']

        for vrsta_indeks in range(self.dimenzija):
            for kolona_indeks in range(self.dimenzija):
                podmatrica = self.tabla.matrica[vrsta_indeks][kolona_indeks]
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if podmatrica[i][j] == igrac:
                            mesto = 3 * (2 - i) + j + 1
                            kolona = kolona_indeks + 1
                            vrsta = chr(vrsta_indeks + 65)
                            for smer in smerovi:
                                potez = vrsta, kolona, mesto, smer
                                svi_potezi.append(potez)
        return svi_potezi
    
    def dobri_losi_potezi(self, igrac):
        svi_potezi = self.svi_potezi_igraca(igrac)
        dobri_potezi, losi_potezi=[],[]
        for potez in svi_potezi:
            if self.provera_poteza(potez):
                dobri_potezi.append(potez)
            else:
                losi_potezi.append(potez)

        print(f"Dobri potezi za igraca {igrac}:")
        for potez in dobri_potezi:
            print(potez)
        
        print(f"Losi potezi za igraca {igrac}:")
        for potez in losi_potezi:
            print(potez)

    def najblizi_stekovi(self, potez):
        potezi={}
        sortirani=[]
        najblizi_stekovi=[]
        vrsta, kolona, mesto, smer = potez
        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1

        udaljenosti=self.udaljenosti_izmedju_figura(self.zauzete_matrice(self.tabla.matrica))
        novi_potez=(chr(indeks_vrste+65), indeks_kolone+1, mesto, '')
        for potez in udaljenosti:
            if potez[0]==novi_potez:
                kljuc=(novi_potez,potez[1])
                vrednost=udaljenosti.get(potez)
                potezi[kljuc]=vrednost
                sortirani = sorted(potezi.items(), key=lambda x: x[1])
        for p in sortirani:
            if p[1]==sortirani[0][1]:#p[1] je rastojanje
                najblizi_stekovi.append(p)
        return sortirani #vraca njabliza rastojanja i polja od njih
    
    def najmanja_rastojanja(self,potez):
        najblizi_stekovi=self.najblizi_stekovi(potez)
        najmanja_rastojanja=[]
        for el in najblizi_stekovi:
            if el[1]==najblizi_stekovi[0][1]:
                najmanja_rastojanja.append(el)
        return najmanja_rastojanja#vraca listu najmanjih rastojanja i njihove matrice
  
    def priblizava_se_steku(self, potez):
        vrsta, kolona, mesto, smer = potez
        iv, ik=self.smerovi(potez)
        nova_vrsta, nova_kolona=chr(iv + 65), ik + 1
        najmanja_rastojanja=self.najmanja_rastojanja(potez)
        element=najmanja_rastojanja[0][0][1]
        v=element[0]
        k=element[1]

        if v != vrsta and k!=kolona:
            if smer=='DD':
                if vrsta <= nova_vrsta <= v and kolona <= nova_kolona <= k:
                    return True
                return False
            if smer=='DL':
                if vrsta <= nova_vrsta <= v and k <= nova_kolona <= kolona:
                    return True
                return False
            if smer=='GD':
                if v <= nova_vrsta <= vrsta and kolona <= nova_kolona <= k:
                    return True
                return False
            if smer=='GL':
                if v <= nova_vrsta <= vrsta and kolona <= nova_kolona <= k:
                    return True
            return False
        else:
            return True     
    
    ##### 3.faza
    def proceni_poteze(self, moguci_potezi):
        ocene={}
        for potez in moguci_potezi:
            ocene[tuple(potez)]=self.oceni_potez(potez)
        return sorted(ocene.items(), key=lambda x:x[1], reverse=True)
    
    def oceni_potez(self, potez):
        nova_vrsta, nova_kolona=self.smerovi(potez)
        if self.provera_poteza(potez):
            sledeca_matrica=self.tabla.matrica[nova_vrsta][nova_kolona]
        return self.brojac_figura(sledeca_matrica)
    
    # # Funkcija koja vraća najbolji potez koristeći Minimax algoritam s Alpha-Beta odsecanjem
    # def minmax_alpha_beta(self, tabla, dubina, maksimizacija, alfa, beta):
    #     if dubina == 0 or self.proveri_kraj_igre():
    #         return(potez, self.oceni_potez(potez))
        
    #     if maksimizacija:
    #         najbolja_ocena = float('-inf')
    #         for potez in self.moguci_potezi_igraca(self.igrac):
    #             nova_tabla = napravi_potez(tabla, potez)#treba da se napravi funkcija za unos poteza od strane racunara
    #             ocena = self.minmax_alpha_beta(nova_tabla, dubina - 1, False, alfa, beta)
    #             najbolja_ocena = max(najbolja_ocena, ocena)
    #             alfa = max(alfa, ocena)
    #             if beta <= alfa:
    #                 break 
    #         return najbolja_ocena
    #     else:
    #         najgora_ocena = float('inf')
    #         for potez in self.moguci_potezi_igraca(self.igrac):
    #             nova_tabla = napravi_potez(tabla, potez)
    #             ocena = self.minmax_alpha_beta(nova_tabla, dubina - 1, True, alfa, beta)
    #             najgora_ocena = min(najgora_ocena, ocena)
    #             beta = min(beta, ocena)
    #             if beta <= alfa:
    #                 break  
    #         return najgora_ocena
        
    # # Funkcija za izvršavanje poteza na tabli
    # def napravi_potez(tabla, potez):
    #     # Implementacija izvršavanja poteza na osnovu trenutne pozicije table
    #     pass

    def igraj(self):
        broj_poteza=0
        print(f"Prvi igrač je {self.igrac}.")

        if self.igrac=='X':
                while True:
                    print(f"Igrač {self.igrac} je na potezu.")
                    self.dobri_losi_potezi(self.igrac)
                    potez = self.unos_poteza()
                    if self.valjanost_poteza(potez):
                        print(self.proveri_kraj_igre())
                        self.pomeri_figure(potez)
                    else:
                        print("Nemoguć potez.")
                        continue

                    print("Trenutna tabla:")
                    self.crtaj_tablu()
                    
                    broj_poteza += 1
                    self.igrac = "X" if broj_poteza % 2 == 0 else "O"

        elif self.igrac=='O':
                while True:
                    print(f"Igrač {self.igrac} je na potezu.")
                    self.dobri_losi_potezi(self.igrac)
                    potez = self.unos_poteza()
                    if self.valjanost_poteza(potez):
                        print(self.proveri_kraj_igre())
                        self.pomeri_figure(potez)
                    else:
                        print("Nemoguć potez.")
                        continue

                    print("Trenutna tabla:")
                    self.crtaj_tablu()

                    broj_poteza += 1
                    self.igrac = "O" if broj_poteza % 2 == 0 else "X"
    
def main():
    igra = Igra()
    igra.postavi_velicinu_table()
    igra.izbor_prvog_igraca()
    igra.postavi_igraca()
    igra.crtaj_tablu()
    igra.igraj()
    
if __name__ == "__main__":
    main()
    