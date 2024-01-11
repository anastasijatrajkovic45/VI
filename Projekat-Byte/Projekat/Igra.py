from functools import cache, reduce
import copy
import random
from Tabla import Tabla

class Igra:
    def __init__(self):
        self.dimenzija = 0
        self.igrac = 'X'
        self.brojac_stack_x = 0
        self.brojac_stack_o = 0
        self.potez = ('', -1, -1, '')
        self.stanja = 0
        self.izbor='covek'
        self.abhash = dict()
        self.odigrani_potezi = 0

    def izbor_prvog_igraca(self):
        while True:
            self.izbor = input("Izaberite ko igra prvi - unesite 'racunar' ili 'covek': ").lower()
            if self.izbor == 'racunar':
                return 'Racunar na potezu'
            elif self.izbor == 'covek':
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
                if len(unos) == 4 and unos[0].isalpha() and unos[1].isdigit() and 0 <= int(unos[2]) <= 7:
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
            else:
                continue
            return potez
    
    def ispravnost_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez
        if kolona < 0 or kolona > self.dimenzija or vrsta<'A' or vrsta > chr(ord('A') + self.dimenzija - 1) or smer not in ['GD', 'GL', 'DD', 'DL']:
            print("Uneli ste pogresnu vrstu, kolonu ili smer.")
        else:
            indeks_vrste = ord(vrsta) - ord('A')
            indeks_kolone = kolona - 1
           
            red_poz, kol_poz = 2 - (mesto // 3), mesto % 3
            matrica_3x3 = self.tabla.matrica[indeks_vrste][indeks_kolone]
            
            for _ in range(2,-1,-1):
                for _ in range(0,3):
                    if matrica_3x3[red_poz][kol_poz] == self.igrac:
                        return True
                    else:
                        print("Na tom mestu se ne nalazi vasa figura.")
                        return False
                
    def proveri_kraj_igre(self):
        broj_figura = self.dimenzija / 2 * (self.dimenzija-2)
        if self.brojac_stack_x >= broj_figura / (2*self.dimenzija) or self.brojac_stack_o >= broj_figura / 2 * self.dimenzija :
            for i in range(len(self.tabla.matrica)):
                for j in range(len(self.tabla.matrica)):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                        self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                        if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                            self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                    else:
                        self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]

            self.crtaj_tablu()

            if self.brojac_stack_x >= broj_figura / (2 * self.dimenzija):
                print('Pobednik je igrač X!')
                return True
            elif self.brojac_stack_o >= broj_figura / (2 * self.dimenzija):
                print('Pobednik je igrač O!')
                return True
        elif self.dimenzija == 10:
            if self.brojac_stack_o >= (broj_figura / (2 * self.dimenzija)) or self.brojac_stack_x == self.brojac_stack_o:
                print('Nereseno')
                return True
        else:
            print("Igra se nastavlja...")
            return False
                
    def brojac_figura(self, matrica3x3):
        brojac = 0
        for i in range(2,-1,-1):
            for j in range(0,3):
                figura = matrica3x3[i][j]
                if figura == 'X' or figura == 'O':
                    brojac += 1
        return brojac
     
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
        red_poz, kol_poz = 2 - (mesto // 3), mesto % 3

        for i in range(red_poz, -1,-1):
                for j in range(kol_poz, 3) if i == 2 - (mesto // 3) else range(0,3):
                    for x in range(2, -1, -1):
                        for y in range(3):
                            if matrica_u[x][y] == '.':
                                element = matrica_iz[i][j]
                                matrica_iz[i][j] = '.'
                                matrica_u[x][y] = element
        return self.tabla.matrica
    
    def valjanost_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez

        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1
        nova_vrsta, nova_kolona = self.smerovi(potez)

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
                
        if indeks_kolone == self.dimenzija-1:
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
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                print("Ne mozete premestiti figuru u tom smeru.")
                return False
                            
        if indeks_kolone == 0:
            matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
            matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
            matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]
            validni_smerovi=['GD', 'DD']

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gd[i][j] == '.' and matrica_dd[i][j] == '.':
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                             return True
            else:
                print("Ne mozete premestiti figuru u tom smeru.")
                return False
        else:
            return True
            
    def dozvoljen_potez(self, potez):
        vrsta, kolona, mesto, smer = potez

        indeks_vrste, indeks_kolone = ord(vrsta) - ord('A'), kolona - 1
        nova_vrsta, nova_kolona = self.smerovi(potez)

        matrica_iz = self.tabla.matrica[indeks_vrste][indeks_kolone]
        matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
        red_poz, kol_poz = 2 - (mesto // 3), mesto % 3
        
        broj_figura_na = 0
        for i in range(red_poz, -1,-1):
            for j in range(kol_poz, 3) if i == 2 - (mesto // 3) else range(0,3):
                figura = matrica_iz[i][j]
                if figura == 'X' or figura == 'O':
                    broj_figura_na += 1

        broj_figura_u = self.brojac_figura(matrica_u)
        broj_figura_iz = self.brojac_figura(matrica_iz) - broj_figura_na

        if broj_figura_u==0:
            return True
        else:
            if broj_figura_u < broj_figura_iz:
                print("Broj figura u steku na kom se premesta figura ili stek treba da bude veci od broja figure u steku sa kog se pomera figura ili stek.")
                return False
            elif(broj_figura_u + broj_figura_na) > 8:
                print("U steku ne može biti više od osam figura. Pokusajte ponovo.")
                return False
            else:
                return True
            
    def provera_poteza(self, potez):
        vrsta, kolona, mesto, smer = potez

        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1
        nova_vrsta, nova_kolona=self.smerovi(potez)

        if nova_vrsta >= 0 and nova_vrsta < self.dimenzija and nova_kolona >= 0 and nova_kolona < self.dimenzija and indeks_kolone > 0 and indeks_kolone < self.dimenzija-1 and indeks_vrste>0 and indeks_kolone< self.dimenzija-1 :
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
               
        if indeks_kolone == self.dimenzija-1:
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
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False
                            
        if indeks_kolone == 0:
            matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
            matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
            matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]
            validni_smerovi=['GD', 'DD']

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gd[i][j] == '.' and matrica_dd[i][j] == '.':
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False
            
        if indeks_vrste == 0:
            matrica = self.tabla.matrica[nova_vrsta][nova_kolona]
            matrica_dd = self.tabla.matrica[indeks_vrste + 1][indeks_kolone + 1]
            matrica_dl = self.tabla.matrica[indeks_vrste + 1][indeks_kolone - 1]
            validni_smerovi=['DL', 'DD']

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_dd[i][j] == '.' and matrica_dl[i][j] == '.':
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False
            
        if indeks_vrste==self.dimenzija-1:
            matrica_gl = self.tabla.matrica[indeks_vrste - 1][indeks_kolone - 1]
            matrica_gd = self.tabla.matrica[indeks_vrste - 1][indeks_kolone + 1]
            validni_smerovi=['GD', 'GL']
            if smer =='GL':
                matrica = self.tabla.matrica[indeks_vrste-1][indeks_kolone-1]
            if smer == 'GD':
                matrica = self.tabla.matrica[indeks_vrste-1][indeks_kolone+1]

            if smer in validni_smerovi:
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if matrica_gl[i][j] == '.' and matrica_gd[i][j] == '.':
                            if self.priblizava_se_steku(potez):
                                return True
                            else:
                                return False
                        elif matrica[i][j] == 'X' or matrica[i][j] == 'O':
                            return True
            else:
                return False


    def da_li_je_stek(self, matrica3x3):
        for i in range(3):
            for j in range(3):
                figura = matrica3x3[i][j]
                if figura == 'X' or figura == 'O':
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
                    zauzeti_indeksi[indeks] = 8 * vrsta_indeks+kolona_indeks+1
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
                            figura = (chr(i + ord('A')), j + 1, 3 * (2 - m) + n, '')
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
    
    def svi_potezi_igraca(self, igrac):
        svi_potezi, smerovi = [], ['GD', 'GL', 'DD', 'DL']

        for vrsta_indeks in range(self.dimenzija):
            for kolona_indeks in range(self.dimenzija):
                podmatrica = self.tabla.matrica[vrsta_indeks][kolona_indeks]
                for i in range(2, -1, -1):
                    for j in range(0, 3):
                        if podmatrica[i][j] == igrac:
                            mesto = 3 * (2 - i) + j 
                            kolona = kolona_indeks + 1
                            vrsta = chr(vrsta_indeks + 65)
                            for smer in smerovi:
                                potez = vrsta, kolona, mesto, smer
                                svi_potezi.append(potez)
        return svi_potezi
    
    def dobri_losi_potezi(self, igrac):
        svi_potezi = self.svi_potezi_igraca(igrac)
        dobri_potezi, losi_potezi = [],[]
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
    
    def dobri_potezi(self, igrac):
        svi_potezi = self.svi_potezi_igraca(igrac)
        dobri_potezi = []
        losi_potezi = []
        for potez in svi_potezi:
            if self.provera_poteza(potez):
                dobri_potezi.append(potez)
            else:
                losi_potezi.append(potez)

        if len(dobri_potezi) == 0:
            dobri_potezi = losi_potezi.copy()

        return dobri_potezi
    
    def najblizi_stekovi(self, potez):
        potezi = {}
        sortirani = []
        najblizi_stekovi = []
        vrsta, kolona, mesto, smer = potez
        indeks_vrste = ord(vrsta) - ord('A')
        indeks_kolone = kolona - 1

        udaljenosti = self.udaljenosti_izmedju_figura(self.zauzete_matrice(self.tabla.matrica))
        novi_potez = (chr(indeks_vrste+65), indeks_kolone+1, mesto, '')
        for potez in udaljenosti:
            if potez[0] == novi_potez:
                kljuc = (novi_potez,potez[1])
                vrednost = udaljenosti.get(potez)
                potezi[kljuc] = vrednost
                sortirani = sorted(potezi.items(), key = lambda x: x[1])
        for p in sortirani:
            if p[1] == sortirani[0][1]:
                najblizi_stekovi.append(p)
        return sortirani
    
    def najmanja_rastojanja(self, potez):
        najblizi_stekovi=self.najblizi_stekovi(potez)
        najmanja_rastojanja = []
        for el in najblizi_stekovi:
            if el[1] == najblizi_stekovi[0][1]:
                najmanja_rastojanja.append(el)
        return najmanja_rastojanja
  
    def priblizava_se_steku(self, potez):
        vrsta, kolona, mesto, smer = potez
        iv, ik = self.smerovi(potez)
        nova_vrsta, nova_kolona = chr(iv + 65), ik + 1
        najmanja_rastojanja = self.najmanja_rastojanja(potez)
        if len(najmanja_rastojanja)==0:
            return True
        element=najmanja_rastojanja[0][0][1]
        v=element[0]
        k=element[1]

        if v != vrsta and k != kolona:
            if smer == 'DD':
                if vrsta <= nova_vrsta <= v and kolona <= nova_kolona <= k:
                    return True
                return False
            if smer == 'DL':
                if vrsta <= nova_vrsta <= v and k <= nova_kolona <= kolona:
                    return True
                return False
            if smer == 'GD':
                if v <= nova_vrsta <= vrsta and kolona <= nova_kolona <= k:
                    return True
                return False
            if smer == 'GL':
                if v <= nova_vrsta <= vrsta and kolona <= nova_kolona <= k:
                    return True
            return False
        else:
            return True     

    def proceni_stanje(self, matrica): #heuristika
        igrac_x_bodovi = 0
        igrac_o_bodovi = 0
        for i in range(self.dimenzija-1):
            for j in range(self.dimenzija-1):
                matrica_3x3 = matrica[i][j]  
                for k in range(3):
                    for l in range(3):
                        if matrica_3x3[k][l] == 'X':
                            igrac_x_bodovi += 1
                        elif matrica_3x3[k][l] == 'O':
                            igrac_o_bodovi += 1
        return igrac_x_bodovi - igrac_o_bodovi
    
    def alphabeta(self, igrac, dubina, alfa, beta, tablehash):
        if tablehash in self.abhash.keys():
            return self.abhash[tablehash]

        if dubina == 0 or not self.proveri_kraj_igre:
            return self.proceni_stanje(self.tabla.matrica)

        if (igrac == 'X'):
            najbolji_potez = -9999
            print(self.dobri_potezi(igrac))
            for x in self.dobri_potezi(igrac):
                pov = self.pomeri_figure(x)
                najbolji_potez = self.alphabeta('O', dubina-1, alfa, beta, self.tabla.get_hash())
                alpha = max(najbolji_potez, alfa)
                if beta <= alpha:
                    break
            self.abhash[tablehash] = najbolji_potez
            return najbolji_potez
        else:
            najbolji_potez = 9999
            for x in self.dobri_potezi(igrac):
                pov = self.pomeri_figure(x)
                najbolji_potez = self.alphabeta('X', dubina-1, alfa, beta, self.tabla.get_hash())
                beta = min(najbolji_potez, beta)
                if beta <= alfa:
                    break
            self.abhash[tablehash] = najbolji_potez
            return najbolji_potez
        
    def sledeci_potez_alpha_beta(self, igrac, dubina):
        potez = ('', -1, -1, '')

        if igrac == 'X':
            moguci_potezi = self.dobri_potezi(igrac)
            print(f"Mogući potezi za {igrac}: {moguci_potezi}")
            najbolji_potez = -9999
            for x in moguci_potezi:
                kopija_stanja = copy.deepcopy(self.tabla.matrica)
                pov = self.pomeri_figure(x)
                score = self.alphabeta('O', dubina - 1, -9999, 9999, self.tabla.get_hash())
                value = max(najbolji_potez, score)

                if value > najbolji_potez:
                    najbolji_potez = value
                    potez = x

                self.tabla.matrica = kopija_stanja
        else:
            moguci_potezi = self.dobri_potezi(igrac)
            print(f"Mogući potezi za {igrac}: {moguci_potezi}")
            najbolji_potez = 9999
            for x in moguci_potezi:
                kopija_stanja = copy.deepcopy(self.tabla.matrica)
                pov = self.pomeri_figure(x)
                score = self.alphabeta('X', dubina - 1, -9999, 9999, self.tabla.get_hash())
                value = min(najbolji_potez, score)

                if value < najbolji_potez:
                    najbolji_potez = value
                    potez = x

                self.tabla.matrica = kopija_stanja   
        return potez

    def postavi_igraca_racunar(self):
        figura = random.choice(['X', 'O'])
        return figura

    def igraj(self):
        broj_figura = self.dimenzija / 2 * (self.dimenzija-2)
        if self.izbor == "covek":
            figura_coveka = self.postavi_igraca()
            figura_racunara = 'O' if figura_coveka == 'X' else 'X'
            self.crtaj_tablu()
        else:
            figura_racunara = self.postavi_igraca_racunar()
            self.crtaj_tablu()
            print(f"Racunar je izabrao figuru: {figura_racunara}")
            figura_coveka = 'O' if figura_racunara == 'X' else 'X'

        if self.izbor == 'covek' or self.izbor == 'racunar':
                while True:
                    if self.izbor == 'covek':
                        self.igrac = figura_coveka
                        print(f"{self.izbor.upper()} je na potezu: {self.igrac}")

                        self.dobri_losi_potezi(self.igrac)
                        potez = self.unos_poteza()
                        nova_vrsta, nova_kolona=self.smerovi(potez)
                        matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
                        if self.valjanost_poteza(potez) and self.dozvoljen_potez(potez):
                                self.pomeri_figure(potez)
                                if self.brojac_figura(matrica_u)==8:
                                    if matrica_u[0][1] == 'X':
                                        self.brojac_stack_x += 1
                                        print(f"Stek pripada igracu X. On ima {self.brojac_stack_x} steka.")
                                        for i in range(0,3):
                                            for j in range(0,3):
                                                matrica_u[i][j] = '.' 
                                    elif matrica_u[0][1] == 'O':
                                        self.brojac_stack_o+=1
                                        print(f"Stek pripada igracu O. On ima {self.brojac_stack_o} steka.")
                                        for i in range(0,3):
                                            for j in range(0,3):
                                                matrica_u[i][j]='.'            
                        else:
                            print("Nemoguć potez.")
                            continue

                        #za kraj
                        if self.igrac=='X': #ako je covek X
                            print(f"Igrac X ima: {self.brojac_stack_x} steka")
                            if self.brojac_stack_x >= broj_figura / (2*self.dimenzija):
                                for i in range(len(self.tabla.matrica)):
                                    for j in range(len(self.tabla.matrica)):
                                        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                            self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                            if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                                self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                        else:
                                            self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                                self.crtaj_tablu()
                                print(f'Pobednik je igrač X: {self.izbor}!')
                                break
                        else: #ako je covek O
                            print(f"Igrac O ima: {self.brojac_stack_o} steka")
                            if self.brojac_stack_o >= broj_figura / (2*self.dimenzija):
                                for i in range(len(self.tabla.matrica)):
                                    for j in range(len(self.tabla.matrica)):
                                        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                            self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                            if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                                self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                        else:
                                            self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                                self.crtaj_tablu()
                                print(f'Pobednik je igrač O: {self.izbor}!')
                                break

                        print("Trenutna tabla:")
                        self.crtaj_tablu()

                    #racunar
                    else:
                        self.igrac=figura_racunara
                        print(f"{self.izbor.upper()} je na potezu: {self.igrac}")
                       
                        potez = self.sledeci_potez_alpha_beta(self.igrac, 1)
                        nova_vrsta, nova_kolona=self.smerovi(potez)
                        matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
                        self.pomeri_figure(potez)
                        if self.brojac_figura(matrica_u) == 8:
                            if matrica_u[0][1] == 'X':
                                self.brojac_stack_x += 1
                                print(f"Stek pripada igracu X. On ima {self.brojac_stack_x} steka.")
                                for i in range(0,3):
                                    for j in range(0,3):
                                        matrica_u[i][j] = '.' 
                            elif matrica_u[0][1] == 'O':
                                    self.brojac_stack_o += 1
                                    print(f"Stek pripada igracu O. On ima {self.brojac_stack_o} steka.")
                                    for i in range(0,3):
                                        for j in range(0,3):
                                            matrica_u[i][j] = '.'

                        if self.igrac=='X': #ako je racunar X
                            print(f"Igrac X ima: {self.brojac_stack_x} steka")
                            if self.brojac_stack_x >= broj_figura / (2*self.dimenzija):
                                for i in range(len(self.tabla.matrica)):
                                    for j in range(len(self.tabla.matrica)):
                                        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                            self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                            if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                                self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                        else:
                                            self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                                self.crtaj_tablu()
                                print(f'Pobednik je igrač X: {self.izbor}!')
                                break
                        else: #ako je racunar O
                            print(f"Igrac O ima: {self.brojac_stack_o} steka")
                            if self.brojac_stack_o >= broj_figura / (2*self.dimenzija):
                                for i in range(len(self.tabla.matrica)):
                                    for j in range(len(self.tabla.matrica)):
                                        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                            self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                            if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                                self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                        else:
                                            self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                                self.crtaj_tablu()
                                print(f'Pobednik je igrač O: {self.izbor}!')
                                break
                
                        print(f"Racunar je odigrao potez: {potez}")

                        print("Trenutna tabla:")
                        self.crtaj_tablu()

                    self.izbor='racunar' if self.izbor=='covek' else 'covek'


#partija izmedju dva coveka
    def igraj_izmedju_dva_coveka(self):
        broj_figura = self.dimenzija / 2 * (self.dimenzija-2)
        print(f"Prvi igrač je {self.igrac}.")

        while True:
                if self.igrac=='X':
                    print(f"{self.izbor.upper()} je na potezu: {self.igrac}")
                    self.dobri_losi_potezi(self.igrac)
                    potez = self.unos_poteza()
                    nova_vrsta, nova_kolona=self.smerovi(potez)
                    matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
                    if self.valjanost_poteza(potez) and self.dozvoljen_potez(potez):
                            self.pomeri_figure(potez)
                            if self.brojac_figura(matrica_u)==8:
                                if matrica_u[0][1] == 'X':
                                    self.brojac_stack_x += 1
                                    print(f"Stek pripada igracu X. On ima {self.brojac_stack_x} steka.")
                                    for i in range(0,3):
                                        for j in range(0,3):
                                            matrica_u[i][j] = '.' 
                                elif matrica_u[0][1] == 'O':
                                    self.brojac_stack_o+=1
                                    print(f"Stek pripada igracu O. On ima {self.brojac_stack_o} steka.")
                                    for i in range(0,3):
                                        for j in range(0,3):
                                            matrica_u[i][j]='.'            
                    else:
                        print("Nemoguć potez.")
                        continue

                    print(f"Igrac X ima: {self.brojac_stack_x} steka")
                    if self.brojac_stack_x >= broj_figura / (2*self.dimenzija):
                        for i in range(len(self.tabla.matrica)):
                            for j in range(len(self.tabla.matrica)):
                                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                    self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                    if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                        self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                else:
                                    self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                        self.crtaj_tablu()
                        print(f'Pobednik je igrač X: {self.izbor}!')
                        break

                    print(f"Igrac O ima: {self.brojac_stack_o} steka")
                    if self.brojac_stack_o >= broj_figura / (2*self.dimenzija):
                        for i in range(len(self.tabla.matrica)):
                            for j in range(len(self.tabla.matrica)):
                                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                    self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                    if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                        self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                else:
                                    self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                        self.crtaj_tablu()
                        print(f'Pobednik je igrač O: {self.izbor}!')
                        break


                    print("Trenutna tabla:")    
                    self.crtaj_tablu()
                else:
                    print(f"{self.izbor.upper()} je na potezu: {self.igrac}")
                    self.dobri_losi_potezi(self.igrac)
                    potez = self.unos_poteza()
                    nova_vrsta, nova_kolona=self.smerovi(potez)
                    matrica_u = self.tabla.matrica[nova_vrsta][nova_kolona]
                    if self.valjanost_poteza(potez) and self.dozvoljen_potez(potez):
                            self.pomeri_figure(potez)
                            if self.brojac_figura(matrica_u)==8:
                                if matrica_u[0][1] == 'X':
                                    self.brojac_stack_x += 1
                                    print(f"Stek pripada igracu X. On ima {self.brojac_stack_x} steka.")
                                    for i in range(0,3):
                                        for j in range(0,3):
                                            matrica_u[i][j] = '.' 
                                elif matrica_u[0][1] == 'O':
                                    self.brojac_stack_o+=1
                                    print(f"Stek pripada igracu O. On ima {self.brojac_stack_o} steka.")
                                    for i in range(0,3):
                                        for j in range(0,3):
                                            matrica_u[i][j]='.'            
                    else:
                        print("Nemoguć potez.")
                        continue

                    print(f"Igrac X ima: {self.brojac_stack_x} steka")
                    if self.brojac_stack_x >= broj_figura / (2*self.dimenzija):
                        for i in range(len(self.tabla.matrica)):
                            for j in range(len(self.tabla.matrica)):
                                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                    self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                    if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                        self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                else:
                                    self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                        self.crtaj_tablu()
                        print(f'Pobednik je igrač X: {self.izbor}!')
                        break

                    print(f"Igrac O ima: {self.brojac_stack_o} steka")
                    if self.brojac_stack_o >= broj_figura / (2*self.dimenzija):
                        for i in range(len(self.tabla.matrica)):
                            for j in range(len(self.tabla.matrica)):
                                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                                    self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]

                                    if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                                        self.tabla.matrica[i][j] = [['.' for _ in range(3)] for _ in range(3)]
                                else:
                                    self.tabla.matrica[i][j] = [[' ' for _ in range(3)] for _ in range(3)]
                        self.crtaj_tablu()
                        print(f'Pobednik je igrač O: {self.izbor}!')
                        break

                    print("Trenutna tabla:")    
                    self.crtaj_tablu()

                self.igrac='O' if self.igrac=='X' else 'X'
    
def main():
    igra = Igra()
    igra.postavi_velicinu_table()
    igra.izbor_prvog_igraca()
    igra.igraj()

    #partija izmedju 2 coveka:
    #igra.crtaj_tablu()
    #igra.igraj_izmedju_dva_coveka()
    
if __name__ == "__main__":
    main()