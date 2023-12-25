def validno(pos: tuple): 
    return 3 > pos[0] >= 0 and 3> pos[1] >= 0 

def polje_ima(pos, vrednost, stanje): 
    return validno(pos) and stanje[pos[0]][pos[1]] is vrednost

def nova_stanja(stanje): 
    for i in range(0, 3): 
        for j in range(0, 3): 
            if polje_ima((i, j), None, stanje): yield(i, j)

def igraj(pos, igrac, stanje): 
    if polje_ima(pos, None, stanje): 
        return[[igrac if pos[0] == j and pos[1] == i else stanje[j][i] for i in range(0, 3)] for j in range(0, 3)]
    return stanje

def kraj(stanje): 
    glavna_dijagonala= [stanje[x][x] for x in range(0, 3)] 
    sporedna_dijagonala= [stanje[x][2-x] for x in range(0, 3)] 
    transponovano_stanje= [[x[pos] for x in stanje] for pos in range(0, 3)] 
    sve= [glavna_dijagonala, sporedna_dijagonala] + stanje+ transponovano_stanje 
    if any([x.count('X') == 3 for x in sve]): 
        return 10
    if any([x.count('O') == 3 for x in sve]): 
        return-10 
    return 0 

def full(stanje): 
    return not any(None in x for x in stanje)

def oceni(stanje): 
    glavna_dijagonala= [stanje[x][x] for x in range(0, 3)] 
    sporedna_dijagonala = [stanje[x][2-x] for x in range(0, 3)] 
    flatten_table= [x for sub_list in stanje for x in sub_list] 
    return(flatten_table.count('X') -flatten_table.count('O') + glavna_dijagonala.count('X') -glavna_dijagonala.count('O') + sporedna_dijagonala.count('X') -sporedna_dijagonala.count('O'))

def max_stanje(lsv): 
    return max(lsv, key=lambda x: x[1]) 

def min_stanje(lsv): 
    return min(lsv, key=lambda x: x[1])

def minimax(stanje, dubina, moj_potez, potez=None): 
    if abs(kraj(stanje)) == 10 or full(stanje): return(potez, kraj(stanje)) 
    igrac= 'X' if moj_potez else 'O' 
    funkcija_min_max= max_stanje if moj_potez else min_stanje 
    lista_poteza= list(nova_stanja(stanje)) 
    if dubina== 0 or lista_poteza is None or len(lista_poteza) == 0: 
        return(potez, oceni(stanje)) 
    return funkcija_min_max([minimax(igraj(x, igrac, stanje), dubina-1, 
        not moj_potez, x if potez is None else potez) for x in lista_poteza])

def max_value(stanje, dubina, alpha, beta, potez=None): 
    if abs(kraj(stanje)) == 10 or full(stanje): 
        return(potez, kraj(stanje)) 
    lista_poteza= list(nova_stanja(stanje)) 
    if dubina== 0 or lista_poteza is None or len(lista_poteza) == 0: 
        return(potez, oceni(stanje)) 
    else: 
        for s in lista_poteza: alpha= max(alpha, min_value(igraj(s, 'X', stanje), dubina-1, alpha, beta, s if potez is None else potez), key=lambda x: x[1]) 
        if alpha[1] >= beta[1]: 
            return beta 
        return alpha
    
def min_value(stanje, dubina, alpha, beta, potez=None): 
    if abs(kraj(stanje)) == 10 or full(stanje): 
        return(potez, kraj(stanje)) 
    lista_poteza= list(nova_stanja(stanje)) 
    if dubina== 0 or lista_poteza is None or len(lista_poteza) == 0: 
        return(potez, oceni(stanje)) 
    else: 
        for s in lista_poteza: 
            beta= min(beta, max_value(igraj(s, 'O', stanje), dubina-1, alpha, beta, s if potez is None else potez), key=lambda x: x[1]) 
            if beta[1] <= alpha[1]: 
                return alpha 
            return beta
        
def minimax_alpha_beta(stanje, dubina, moj_potez, alpha=(None, -10), beta=(None, 10)): 
    if moj_potez: 
        return max_value(stanje, dubina, alpha, beta) 
    else:
        return min_value(stanje, dubina, alpha, beta)
    
def print_repr(symbol): 
    return(f'{symbol}' if symbol in[X, O] else' ')    

def print_table(stanje: list[list]): 
    board= [print_repr(x) for y in stanje for x in y]

def igra(tabla, igrac, potez): 
    print_table(tabla) 
    while(kraj(tabla) == 0 and not full(tabla)):
         # dubina je u ovom slučaju 9, ali može da bude i manja 
        min_max_result = minimax(tabla, 9, potez) 
        min_max_alpha_beta_result = minimax_alpha_beta(tabla, 9, potez) 
        print(f"Min-Max: {min_max_result}") 
        print(f"Min-Max α-β: {min_max_alpha_beta_result}") 
        naj = min_max_result[0] if type(min_max_result) is tuple else (0, 0) 
        tabla = igraj(naj, igrac, tabla) 
        print_table(tabla) 
        igrac = 'O' if igrac == 'X' else 'X' 
        potez= not potez 
    pobednik = ('X' if kraj(tabla) == 10 else 
               ('O' if kraj(tabla) == -10 else 
                "Nerešeno")) 
    print(f"Pobednik je: {pobednik}")

    tabla = [[None, None, None], [None, None, None], [None, None, None]] 
    igrac = ('X' if input("Uneti igrača: ") == "X" else 'O') 
    potez = True if igrac == 'X' else False 
    igra(tabla, igrac, potez)