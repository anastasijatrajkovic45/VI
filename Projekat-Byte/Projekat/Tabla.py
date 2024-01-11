from functools import reduce
import string

class Tabla:
    def __init__(self, dimenzija) -> None:
        self.dimenzija = dimenzija
        self.matrica = []
        self.matrica_3x3_tacka = [['.' for _ in range(3)] for _ in range(3)]
        self.matrica_3x3_prazna = [[' ' for _ in range(3)] for _ in range(3)]
        self.played_x = set()
        self.played_o = set()

        for i in range(self.dimenzija):
            red = []
            for j in range(self.dimenzija):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    self.matrica_3x3 = [['.' for _ in range(3)] for _ in range(3)]

                    if (i == 0 or i == self.dimenzija-1) and (i + j + 1) % 2 == 1:
                        self.matrica_3x3 = [['.' for _ in range(3)] for _ in range(3)]

                    elif i % 2 == 1 and (i + j + 1) % 2 == 1 and i != self.dimenzija - 1:
                        self.matrica_3x3[2][0] = 'X'

                    elif i % 2 == 0 and (i + j) % 2 == 0 and i not in [0, self.dimenzija]:
                        self.matrica_3x3[2][0] = 'O'
                else:
                    self.matrica_3x3 = [[' ' for _ in range(3)] for _ in range(3)]

                red.append(self.matrica_3x3)
            self.matrica.append(red)

    def iscrtaj_tablu(self):
        
        print(f"TABLA {self.dimenzija}x{self.dimenzija}")

        print('       ', end='')
        for broj in range(1, self.dimenzija + 1):
            print(broj, end='     ')
        print()

        slova = string.ascii_uppercase[:self.dimenzija]
        for j, red in enumerate(self.matrica):
            for i in range(3):
                if i == 1:
                    print(f' {slova[j]} ', end='  ')
                else:
                    print('    ', end=' ')
                for elem in red:
                    print(' '.join(elem[i]), end=' ')
                print()
    
    def get_hash(self):
        return (reduce(lambda a, b: a * (b[0]+1) * (b[1]+1), self.played_x, 1), reduce(lambda a, b: a * (b[0]+1) * (b[1]+1), self.played_o, 2))