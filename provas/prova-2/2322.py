# Eduardo Zanetta - 20203087 // Turma 01208B

# input do usuário
n = int(input())

# declarando somadores
sum = 0
sum2 = 0

# somando todos os números no intervalo [1, n]
for x in range(1, n + 1):
    sum += x

# input das peças q faltam
pieces = input().split()

for x in range(0, n - 1):
    pieces[x] = int(pieces[x]) # declarando como int para poder somar futuramente
    sum2 += pieces[x] # somando peças presentes

# como as peças sao numeradas começando pelo 1, a lógica é: o numero da peça faltante é = a soma de todas as peças menos a soma das presentes
print(sum - sum2)
    
