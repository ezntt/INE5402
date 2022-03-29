# Eduardo Zanetta - 20203087

while True:

    bills = [2, 5, 10, 20, 50, 100] # Notas disponíveis

    possible = False
    
    price, paid = input().split() # Input do usuário

    price = int(price) # Conversão para int
    paid = int(paid)

    change = paid - price # Troco

    if price == 0 and paid == 0: # Encerra programa
        break

    for i in range(0, len(bills)):

        for j in range(0, len(bills)):

            if bills[i] + bills[j] == change: # Laço testa todas as somas entre dois números entre as notas presentes na lista e confere se a soma é igual ao troco exato
                possible = True

    print('possible') if possible else print('impossible') # Output condicional



