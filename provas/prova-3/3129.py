# Eduardo Zanetta - 20203087

# código adaptado da questão 2410

# entrada
n = int(input())

# criando array
stickers = []

# contador começa em n
counter = n

# input dos registros dos alunos
for i in range(0, n):
    stickers.append(int(input()))

# organizando números de registro em ordem
sorted_stickers = sorted(stickers)

# verificação se há números repetidos
for i in range(0, n):
    if (i < n - 1): # prevenindo "list index out of range"
        if sorted_stickers[i] == sorted_stickers[i+1]:
            counter -= 1 # caso há repetidos, diminuir 1 do número total

# output
print(counter) # diferentes
print(n - counter) # repetidas
