# Eduardo Zanetta - 20203087 // Turma 01208B

# aposta de flavinho
f = input().split()

# numeros sorteados 
s = input().split()

# contador
counter = 0

# somando itens iguais ao contador
for i in range(len(f)):
    counter += s.count(f[i])

# condicionais para imprimir o caso
if counter == 3:
    print('terno')

elif counter == 4:
    print('quadra')

elif counter == 5:
    print('quina')

elif counter == 6:
    print('sena')

else: 
    print('azar') 