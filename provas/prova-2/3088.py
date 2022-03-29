# Eduardo Zanetta - 20203087 // Turma 01208B

while True:

    try:

        # input do usuario
        r = input()

        # converte input para string
        r = str(r)

        # substituições
        r = r.replace(' .', ".").replace(' ,', ',') 

        print(r)
        
    # finaliza a correção
    except EOFError:
        break