#Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja kreira listu N tuple
#obekata. Prvi element u svakom tuple objektu je redni broj tog tuple objekta a drugi
#kvadrat zbira svih indeksa od 0 do trenutnog indeksa.
#Primer: kreiraj(4) = [(0, 0), (1, 1), (2, 9), (3, 36), (4, 100)]
def kreiraj(n):
    i=0
    lista=[]
    suma=0
    while i<=n:
        suma+=i
        kvadratZ=suma**2
        tuple1=(i,kvadratZ)
        lista.append(tuple1)
        i+=1
    print(lista)

kreiraj(4)
