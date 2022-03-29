# Eduardo Zanetta - 20203087

# entrada ('S' ou qualquer outra coisa para 'M')
op = input().upper()

# declarando variaveis (soma e contador de números válidos começam em 0)
sum = 0
validcounter = 0

# ordem da matriz
order = 12

# preenchendo primeira linha da matriz com None
matrix = [None] * order

# preenchendo colunas da matriz com None
for i in range(0, order):
    matrix[i] = [None] * order

# preenchimento da matriz pelo input do usuário, elemento por elemento
for i in range(0, order):
    for j in range(0, order):
        matrix[i][j] = float(input())

# considerando apenas a área inferior, como a questão solicita
for i in range(0, order):
    for j in range(0, order): 
        if i > j: # abaixo da diagonal principal
            if i + j > order - 1: # abaixo da diagonal secundária (o certo seria "order + 1", mas como arrays começam em 0, tornou-se "order + 1 - 2", no caso "order - 1")
                validcounter += 1 # contador de elementos válidos
                sum += matrix[i][j] # somando elementos válidos

# output desejado
if op == 'S':
    print(sum)
else:
    print(sum / validcounter)