# -*- coding: utf-8 -*-

# inputs do usuario / idades
monica = int(input())
filho1 = int(input())
filho2 = int(input())

# cálculo da idade do filho 3 (não necessariamente o mais velho)
filho3 = monica - (filho1 + filho2)

# função nativa do python que recebe o maior valor entre os argumentos
maisvelho = max(filho1, filho2, filho3)

print(maisvelho)