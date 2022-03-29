# Eduardo Zanetta - 20203087 // Turma 01208B

# input do usuário
n, i, f = input().split()

n = int(n)
i = int(i)
f = int(f)

v = input().split() # entrada com os n inteiros descritos acima 

# declarando array
p = []

# total de pares possiveis na entrada
for i in range(len(v)):

    for j in range (i + 1, len(v)):

        # transformando em inteiros
        s = int(v[i]), int(v[j])

        p.append(s)       

# declarando contador
counter = 0

for i in range(len(p)):

    # soma dos numeros em cada par
    soma = sum(p[i])

    # verificando se atende os requisitos
    if (i <= soma <= f):
        counter += 1
        
# imprime o contador
print(counter)