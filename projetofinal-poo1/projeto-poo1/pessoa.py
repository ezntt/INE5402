funcionarios = []
clientes = []

# chefe já é pré definido no programa
chefe = {'nome':'Eduardo', 'cpf':'11184024496', 'senha':'123'}

class Pessoa:

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def validar_chefe(cpf):

        if cpf == chefe['cpf']: # procura na lista
            senha = input(f"Olá {chefe['nome']}, digite sua senha para prosseguir: ")

            if senha == chefe['senha']:
                return True

            else:
                print("Senha incorreta.")
                return False

        else:
            print("CPF inválido.")
            return False

    def validar_funcionario(cpf):

        for i in range(0, len(funcionarios)):

            if cpf == funcionarios[i]['cpf']:
                senha = input(f"Olá {funcionarios[i]['nome']}, digite sua senha para prosseguir: ")
                
                if senha == funcionarios[i]['senha']:
                    return True
                else:
                    print("Senha incorreta.")
                    return False
        

class Chefe(Pessoa):

    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha) # Herda atributos da classe Pessoa

    def existem_funcionarios():

        if len(funcionarios) == 0:
            print("Não há funcionários na sua empresa.")
            return False
        else:
            return True

    def mostrar_funcionarios():
        
        print("LISTA DE FUNCIONÁRIOS -----")
        for i in range(0, len(funcionarios)):
            print(f"{i + 1} - {funcionarios[i]['nome']}") 

    def add_funcionario(nome, cpf, senha):
        funcionarios.append({'nome':nome, 'cpf':cpf, 'senha':senha})
        print(f"{nome} agora é um funcionário!")

    def obedece_index(index):
        if index <= len(funcionarios) and index > 0:
            return True
        else:
            print("Digite um número válido")
            return False

    def rem_funcionario(index):

        if Chefe.obedece_index(index):
            print(f"Funcionário {funcionarios[index - 1]['nome']} demitido.")
            funcionarios.pop(index - 1)
        
    def trocar_senha_funcionario(index, senha):

        if Chefe.obedece_index(index):
            funcionarios[index - 1]['senha'] = senha
            print(f"Senha do funcionário {funcionarios[index - 1]['nome']} alterada com sucesso.")

    def validar_senha(senha):
        
        senha_atual = chefe['senha']

        if senha == senha_atual:
            return True
        else:
            print("Senha incorreta.")
            return False
            
    def trocar_senha(nova_senha):
        chefe['senha'] = nova_senha

    def mostrar_dados():
        
        print(f"CHEFE: {chefe['nome']}, CPF: {chefe['cpf']}")

        print(f"FUNCIONÁRIOS:")
        for i in range(0, len(funcionarios)):
            print(f"{i + 1} - {funcionarios[i]['nome']}, CPF: {funcionarios[i]['cpf']}")
        
        print(f"CLIENTES:")
        for i in range(0, len(clientes)):
            print(f"{i + 1} - {clientes[i]['nome']}, CPF: {clientes[i]['cpf']}")

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)

    def existem_clientes():

        if len(clientes) == 0:
            print("Não há clientes disponíveis.")
            return False
        else:
            return True

    def mostrar_clientes():

        print("LISTA DE CLIENTES -----")
        for i in range(0, len(clientes)):
            print(f"{i + 1} - {clientes[i]['nome']}") 

    def add_cliente(nome, cpf):
        clientes.append({'nome':nome, 'cpf': cpf})
        print(f"Cliente {nome} adicionado com sucesso!")
    
    def rem_cliente(index):
        print(f"Cliente {clientes[index - 1]['nome']} removido.")
        clientes.pop(index - 1)
