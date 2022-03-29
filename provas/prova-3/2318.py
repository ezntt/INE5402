# Eduardo Zanetta - 20203087

order = 3
sum = 0

otarr = []

matrix = [None] * order

for i in range(0, order):
    matrix[i] = input().split()

    for j in range(0, order):
        matrix[i][j] = int(matrix[i][j])

# checando se há 0 nas linhas
for i in range(0, order):

    for j in range(0, order):

        if 0 not in matrix[i]:
            otarr.append(matrix[i][j])
            break

print(otarr)

# 1. ver se tem 0 nas linhas