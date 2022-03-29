from pessoa import *

while True:

    # comandos iniciais
    op = int(input('\n======= MENU PRINCIPAL =======\n'
                   '< 1 > Login como CHEFE\n'
                   '< 2 > Login como FUNCIONÁRIO\n'
                   '< 0 > SAIR DO PROGRAMA\n\n'
                   '-> '))

    # LOGIN DO CHEFE
    if op == 1:

        cpf = input('===== LOGIN CHEFE =====\n\n'
                    'Digite seu CPF: ')

        # cpf e senha validados
        if Pessoa.validar_chefe(cpf):
        
            # laço para quando o chefe acabar a operação, não voltar direto para o menu principal
            while True:

                    op_chefe = int(input('\n======= MENU CHEFE =======\n'
                                        '< 1 > Cadastrar funcionário\n'
                                        '< 2 > Demitir funcionário\n'
                                        '< 3 > Alterar senha de funcionário\n'
                                        '< 4 > Alterar sua senha\n'
                                        '< 5 > Mostrar dados da empresa\n'
                                        '< 0 > SAIR DO MENU CHEFE\n\n'
                                        '-> '))
                    
                    # opção de cadastrar o funcionário
                    if op_chefe == 1:

                        nome = input("Nome do novo funcionário: ")
                        cpf = input("CPF do novo funcionário: ")
                        senha = input("Senha do novo funcionário: ")

                        # criando novo funcionário
                        Chefe.add_funcionario(nome, cpf, senha)
                        
                    
                    # opção de remover funcionário
                    if op_chefe == 2:
                        
                        # antes de demitir algum funcionario, certificar de que a lista de funcionários não se encontra vazia
                        if Chefe.existem_funcionarios():

                            # lista funcionários
                            Chefe.mostrar_funcionarios()

                            while True:
                                try:
                                    
                                    index = int(input("Digite o número correspondente ao funcionário que deseja demitir: "))
                                    
                                    Chefe.rem_funcionario(index)

                                    break
                                except ValueError:
                                    print("Digite um número válido: ")
                    
                    # opção de alterar senha de funcionário
                    if op_chefe == 3:

                        if Chefe.existem_funcionarios():
                        
                            Chefe.mostrar_funcionarios()

                            while True:
                                try:
                                    index = int(input("Digite o número correspondente ao funcionário que deseja trocar a senha: "))
                                    
                                    break
                                except ValueError:
                                    print("Digite um número válido: ")
                            
                            nova_senha = input("Digite a nova senha para o funcionário escolhido: ")
                            
                            # altera senha do funcionário escolhindo
                            Chefe.trocar_senha_funcionario(index, nova_senha)

                    # opção de alterar a propria senha
                    if op_chefe == 4:

                        senha = input("Senha atual: ")

                        # verifica se chefe realmente sabe a sua senha
                        if Chefe.validar_senha(senha):
                            nova_senha = input("Nova senha: ")

                            Chefe.trocar_senha(nova_senha) 

                            print("Senha alterada com sucesso.")
                        else:
                            print("Senha incorreta.")

                    if op_chefe == 5:
                        Chefe.mostrar_dados()
                    
                    # encerra programa
                    if op_chefe == 0:
                        break
                            

    # LOGIN DO FUNCIONARIO
    if op == 2:
        
        cpf = input("Digite seu CPF: ")

        # cpf e senha validados
        if Pessoa.validar_funcionario(cpf):

            # laço para quando o funcionario acabar a operação, não voltar direto para o menu principal
            while True: 

                op_funcionario = int(input('\n======= MENU FUNCIONARIO =======\n'
                                        '< 1 > Cadastrar cliente\n'
                                        '< 2 > Remover cliente\n'
                                        '< 0 > SAIR\n'
                                        '-> '))
            
                if op_funcionario == 1:

                    nome = input("Nome do novo cliente: ")
                    cpf = input("CPF do novo cliente: ")

                    Funcionario.add_cliente(nome, cpf)

                if op_funcionario == 2:

                    if Funcionario.existem_clientes():
                        
                        Funcionario.mostrar_clientes()

                        while True:
                            try:
                                
                                index = int(input("Digite o número correspondente ao cliente que deseja remover: "))
                                
                                Funcionario.rem_cliente(index)

                                break
                            except ValueError:
                                print("Digite um número válido: ")

                if op_funcionario == 0:
                    break

    # encerra programa
    if op == 0:
        break

    