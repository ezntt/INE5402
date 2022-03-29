# Eduardo Zanetta - 20203087

while True: # Laço para repetir programa

    counters = [ # Dicionário para melhor organização (não sei se era realmente necessário)
        {'num': 0, 'counter': 0},
        {'num': 1, 'counter': 0},
        {'num': 2, 'counter': 0},
        {'num': 3, 'counter': 0},
        {'num': 4, 'counter': 0},
        {'num': 5, 'counter': 0},
        {'num': 6, 'counter': 0},
        {'num': 7, 'counter': 0},
        {'num': 8, 'counter': 0},
        {'num': 9, 'counter': 0}
    ]

    frequency = [0] * 10 # Criando array com frequencias, com seus valores iguais à key 'counter'

    most_frequent = 0 # Declarando variável de número mais frequente

    try:
        numbers = list(map(int, input())) # Input do usuário, adicionando todos os numeros em uma lista e convertendo para int com o map

        for i in range(0, len(numbers)): # Dois laços percorrendo todos os números digitados e vendo se corresponde aos digitos [0, 9]

            for j in range(0, 10):
                
                if numbers[i] == j:
                    counters[j]['counter'] += 1 # Acrescentando 1 a mais na frequência dos números

        for i in range(0, 10):
            frequency[i] = counters[i]['counter'] # Adicionando valores ao array de frequências
        
        for i in range(0, 10):
            if counters[i]['counter'] == max(frequency): # Função max() = retorna maior valor (no caso a maior frequência)
                most_frequent = counters[i]['num'] # Atualizando valor do número frequente mais presente

        print(most_frequent) # Output

    except EOFError: # Fim de arquivo
        break