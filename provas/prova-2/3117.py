# Eduardo Zanetta - 20203087 // Turma 01208B

# input do usuario
n, k = input().split()

# convertendo para int
n = int(n)
k = int(k)

counter = 0

# input das horas que os alunos chegam
h = input().split()

for i in range(n):

    # convertendo para int
    h[i] = int(h[i])

    if h[i] <= 0: #requisito minimo de horario

        # adicionando ao contador
        counter += 1

# saídas
if counter >= k:
    print('YES')

else:
    print('NO')