# Eduardo Zanetta - 20203097

n, m, s = input().split()
n = int(n)
m = int(m)
s = int(s)

soldier_counter = 0

matrix = [None] * 3

for i in range(0, 3):

    matrix[i] = input().split()

    for j in range(0, s):
        matrix[i][j] = int(matrix[i][j])



# contador de soldados
for i in range(0, s):
    soldier_counter += matrix[i][2]

print(soldier_counter)

