# Eduardo Zanetta - 20203087

h_bonecos = 0
h_arquitetos = 0
h_musicos = 0
h_desenhistas = 0

qtd_elfos = int(input()) # Input da quantidade de elfos 


elfos = [] # Lista de elfos (lista de dicionários)

for i in range(0, qtd_elfos):
    nome, grupo, horas = input().split() # Input do usuário

    for j in range(0, qtd_elfos): # Transforma as horas em tipo int
        horas = int(horas)

    elfos.append({'nome': nome, 'grupo': grupo, 'horas': horas}) # Adicionando dicionário à lista

for i in range(0, qtd_elfos): # Separando as horas para cada função

    if elfos[i]['grupo'] == 'bonecos':
        h_bonecos += elfos[i]['horas']

    elif elfos[i]['grupo'] == 'arquitetos':
        h_arquitetos += elfos[i]['horas']

    elif elfos[i]['grupo'] == 'musicos':
        h_musicos += elfos[i]['horas']

    elif elfos[i]['grupo'] == 'desenhistas':
        h_desenhistas += elfos[i]['horas']

total_presentes = (h_bonecos // 8) + (h_arquitetos // 4) + (h_musicos // 6) + (h_desenhistas // 12) # Fórmula com as divisões exatas

print(total_presentes) # Output