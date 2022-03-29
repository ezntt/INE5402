# -*- coding: utf-8 -*-

# input do usuario
bolinhas = int(input())
galhos = int(input())

# operação para verificar se não tenha mais que a metade de galhos em bolinhas
# operação "//" faz com que arredonde para baixo (floor division)
if (galhos // 2) <= bolinhas:
    print("Amelia tem todas bolinhas!")
    
else:
    print(f"Faltam {galhos // 2 - bolinhas} bolinha(s)")