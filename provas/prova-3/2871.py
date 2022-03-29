# Eduardo Zanetta - 20203087

while True:
    try:

        # input
        rows, columns = input().split()

        # convertendo para int
        rows = int(rows)
        columns = int(columns)

        # declarando variaveis
        bags = 0
        liters = 0
        sum = 0

        # criação da matriz
        matrix = [None] * rows

        # preenchendo matriz
        for i in range(0, rows):
            
            matrix[i] = input().split()
            
            for j in range(0, columns):
                matrix[i][j] = int(matrix[i][j])

        # somando elementos da matriz
        for i in range(0, rows):
            for j in range(0, columns):
                sum += matrix[i][j]

        # condições para contar número de sacas e de litros
        if sum >= 60:
            bags = sum // 60
            liters = sum % 60
        else:
            bags = 0
            liters = sum

        # output
        print(f'{bags} saca(s) e {liters} litro(s)')

    # end of file
    except EOFError:
        break