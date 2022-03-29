# -*- coding: utf-8 -*-

# entrada da quantidade de ingredientes
# input do tipo split (na mesmin_f linha)
# f = farinha / o = ovos / l = leite
f, o, l = input().split()
f = int(f)   
o = int(o)
l = int(l)

# proporçoes
# menores valores para cada ingrediente, visto que o bolo necessita de:
min_f = f // 2 # 2 xicaras de farinha
min_o = o // 3 # 3 ovos   
min_l = l // 5 # 5 colheres de leite

# condiçao caso as divisoes façam com que tenham a quantidade exata de ingredientes necessaria para o(s) bolo(s)
if (f % 2 == 0) and (o % 2 == 0) and (l % 2 == 0): 

    if (min_o >= min_f) and (min_f >= min_l):
        print(min_f)

    elif (min_f >= min_o) and (min_l >= min_o):
        print(min_o)
        
    elif (min_f >= min_l) and (min_o >= min_l):
        print(min_l)

# condiçao caso as divisoes NÃO façam com que tenham a quantidade exata de ingredientes necessaria para o(s) bolo(s)
# a menor quantidade de bolos possível será feita
else:

    if (min_o >= min_f) and (min_l >= min_f):
        print(min_f)

    elif (min_f >= min_o) and  (min_l >= min_o):
        print(min_o)

    elif (min_o >= min_l) and (min_f >= min_l):
        print(min_l)