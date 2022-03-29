# -*- coding: utf-8 -*-

# input do tipo split
n, m = input().split()
n = int(n)
m = int(m)

# contadores
counter1 = 0
counter2 = 0

# código repete até achar o primo mais próximo, incrementando em 1 sempre
while counter1 <= n:

    # numero de divisores
    divisores = 0
    
    for x in range(1, n + 1):
        
        # se n for divisível por x, contar 1 ao número de divisores
        if (n % x == 0):
            divisores += 1

    # caso seja primo, encerra o loop
    # 2 divisores naturais = numero é primo (1 e ele mesmo)
    if divisores == 2:
        break

    # caso não seja primo, diminuir 1 de n
    else:
        n -= 1
    
    counter1 += 1

# igual a linha 11 - 31, porém trocando 'n' por 'm'
while counter2 <= m:

    divisores = 0
    
    for x in range(1, m + 1):
        
        if (m % x == 0):
            divisores += 1

    if divisores == 2:
        break

    else:
        m -= 1
    
    counter2 += 1

# multiplicação dos números primos encontrados
print (n * m)

