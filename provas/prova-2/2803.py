# Eduardo Zanetta - 20203087 // Turma 01208B

# declarando estados da regiao norte
estados = ['acre', 'amapa', 'amazonas', 'para', 'rondonia', 'roraima', 'tocantins']

# input do usuário
estado = input()

# declarando inicialmente como se não pertencesse
pertence = False

# comparando estado do input com algum do array
for i in range(len(estados)):

    if estado == estados[i]: 
        pertence = True

# caso pertence
if pertence:
    print("Regiao Norte")

# caso nao pertencesse
else:
    print("Outra regiao")