# Eduardo Zanetta - 20203087

n, m = input().split()
n = int(n)
m = int(m)

matrix = [None] * n

for i in range(0, n):

    matrix[i] = input().split()

    for j in range(0, m):

        matrix[i][j] = int(matrix[i][j])

for i in range(0, n):
    if 0 in (matrix[i]):
        if i < n - 1:
            if 0 in (matrix[i + 1]):
                print('teste')