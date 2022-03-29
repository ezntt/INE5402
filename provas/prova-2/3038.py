# Eduardo Zanetta - 20203087 // Turma 01208B

while True:

    try:

        # input do usuario
        f = input()

        # converte input para string
        f = str(f)

        # substituições
        f = f.replace('@', "a").replace('&', 'e').replace('!', 'i').replace('*', 'o').replace('#', 'u')

        print(f)
        
    # finaliza a correção
    except EOFError:
        break