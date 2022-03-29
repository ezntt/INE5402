# -*- coding: utf-8 -*-

# input do usuario
n = int(input())

# valores de gastos e verba serao preenchidos pelo usuario posteriornmente
tot_gastos = 0
tot_verba = 0

for x in range(0, n):
    
    # input do usuario, sendo eles gasto ou verba e o valor, respectivamente
    t, c = input().split()
    c = int(c)
    
    # adicionando valor inserido ao total de gastos
    if (t == "G"):
        tot_gastos += c
    
    # adicionando valor inserido ao total de verba
    elif (t == "V"):
        tot_verba += c
        
# caso o governo banque os valores suficientes para cobrir os gastos
if (tot_verba >= tot_gastos):
    print("A greve vai parar.")
    
# caso isso não aconteça
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")