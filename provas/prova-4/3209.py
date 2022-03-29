# Eduardo Zanetta - 20203087

n = int(input()) # Input do usuário

for i in range(0, n):
    
    k = [int(x) for x in input().split()] # Input dos filtros de linha
    
    sum = 0 # Declarando somador
    
    filter = k[0] # Quantidade de filtros na primeira posição da lista

    for j in range(1, filter + 1): # Laço iniciando em 1 pois os filtros começam em 1
        sum += k[j] # Adicionando o valor ao somador
        
        print(sum - (filter - 1)) # Output removendo o filtro que está na tomada e os conectados também