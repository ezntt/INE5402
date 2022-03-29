# Eduardo Zanetta - 20203087

n = int(input()) # Input do usuário

cards = [] # Criando lista de cartas (montes)

for i in range(0, n):
    cards.append(input()) # Adicionando input das cartas à lista

for i in range(0, n):
    
    if 'Q' not in cards[i] or 'J' not in cards[i] or 'K' not in cards[i] or 'A' not in cards[i]: # Caso algumQ J K A não estejam presentes
        print('Ooo raca viu')
    else: # Caso todos estejam presentes
        print('Aaah muleke')