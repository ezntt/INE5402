# Eduardo Zanetta - 20203087

# entrada
n = int(input())

# criando array
students = []

# contador começa em n
counter = n

# input dos registros dos alunos
for i in range(0, n):
    students.append(int(input()))

# organizando números de registro em ordem
sorted_students = sorted(students)

# verificação se há números repetidos
for i in range(0, n):
    if (i < n - 1): # prevenindo "list index out of range"
        if sorted_students[i] == sorted_students[i+1]:
            counter -= 1 # caso há repetidos, diminuir 1 do número total

# output
print(counter)
