# Eduardo Zanetta - 20203087 // Turma 01208B

# input do usuario
n = int(input()) 

# declarando arrays
c = []

for i in range(n):
    c += input().split() #unifica a lista de crianças e identificaçao 

# contadores
femcounter = c.count('F')
malecounter = c.count('M')

# num de carrinhos e bonecas
print(f'{malecounter} carrinhos')
print(f'{femcounter} bonecas')