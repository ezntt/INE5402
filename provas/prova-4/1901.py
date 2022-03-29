# Eduardo Zanetta - 20203087

order = int(input()) # Ordem da matriz da floresta

first_matrix = [None] * order # Matriz da floresta

counter = [] # Matriz das celulas visitadas

for i in range(0, order):
    first_matrix[i] = input().split() # Input das espécies na matriz

    for j in range(0, order): # Convertendo para int
        first_matrix[i][j] = int(first_matrix[i][j]) 

for i in range(0, order * 2):
    n, m = input().split() # Input das células visitadas

    for j in range(0, order * 2): # Convertendo para int
        n = int(n)
        m = int(m)

    counter.append(first_matrix[n - 1][m - 1]) # Adicionando células visitadas na sua matriz (n-1 pois a posição 1 1 na verdade é 0 0)

print(len(set(counter))) # Output do tamanho da matriz de células visitadas, com o set() (função nativa do python) removendo elementos repetidos