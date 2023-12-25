#Korišdenjem programskog jezika Python, napisati funkciju uredi, koja svaki od prvih N
# elemenata uvedava za definisanu vrednost a preostale umanjuje za definisanu vrednost.
# Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost koja treba da
# se uvedava, odnosno umanjuje.
# Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]

def uredi(lista,n, vrednost):
    lista[0:n]=[el+vrednost for el in lista[0:n]]
    lista[n:]=[el-vrednost for el in lista[n:]]
    print(lista)
    
uredi([1, 2, 3, 4, 5], 3, 1)

#def uredi(lista,n, vrednost):
   # for i in range(len(lista)-1):
   #     if i<n:
    #        lista[i]+=vrednost
   #     else:
  #          lista[i]-=vrednost
 #   print(lista)

#uredi([1, 2, 3, 4, 5], 3, 1)