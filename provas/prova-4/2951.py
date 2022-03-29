# Eduardo Zanetta - 20203087

n, g = input().split() # Input do número de tentativas e os pontos a serem batidos
n = int(n)
g = int(g)

sum = 0 # Somador começando em 0

inputs = [] # Lista de inputs das proximas n linhas

for i in range(0, n):
    rune, points = input().split() # Inputs do usuario
    points = int(points) # Convertendo os segundos inputs de cada linha para int para realizar a soma futuramente

    inputs.append({'rune': rune, 'points': points}) # Salvando runas e pontos na lista de inputs, para melhor manipulação


x = int(input()) # Número de runas utilizadas na "batalha"

runes = list(map(str, input().strip().split()))[:x] # Múltiplos inputs na mesma linha armazenados em um array de tamanho x

'''
list() = transforma em array

map() = aplica uma função em cada item de uma lista, sendo a função o primeiro argumento e a lista o segundo
    map está convertendo cada item 'input().strip().split()' em 'str'

strip() = não entendi perfeitamente, mas creio que remove espaços adicionais (ex: "   banana   " -> "banana")

[:x] = tamanho da lista
'''

for i in range(0, len(runes)):
    
    for j in range(0, len(inputs)): # Dois laços para verificação em duas listas diferentes
        
        if runes[i] == inputs[j]['rune']: # Condicional caso runa da lista runes seja igual às runas dos inputs

            sum += inputs[j]['points'] # Adicionando pontos ao somador

print(sum) # Output
print('You shall pass!') if sum >= g else print('My precioooous') # Outputs condicional