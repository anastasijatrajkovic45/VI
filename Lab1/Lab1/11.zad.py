#Korišdenjem programskog jezika Python, napisati funkciju razlika, koja kreira novu listu čiji
# su elementi razlika susednih elementa liste.
# Primer: razlika([8, 5, 3, 1, 1]) = [3, 2, 2, 0]
def razlika(lista):
    novaLista=[]
    novaLista=[lista[i]-lista[i+1] for i in range(len(lista)-1)]
    print(novaLista)

razlika([8, 5, 3, 1, 1])
