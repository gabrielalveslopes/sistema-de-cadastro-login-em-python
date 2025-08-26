import re #serve pra colocar regras de segurança, sem a precisar escrever de linhas de código para checar cada caractere individualmente.

usuarios = {}  # Dicionário para armazenar login e senha

def cadastrar():
    print('--- Cadastro ---') # cria um titulo pra parte de cadastro
    usuario = input('Digite um nome de usuário: ') #pede pro usuario colocar seu nome
    
    if usuario in usuarios: #verifica se ja existe aquele nome de usuario dentro do dicionario cadastro
        print('Usuário já existe! Tente outro.')
        return #encerra a função se usuario existir, voltando para o menu

    while True:  # laço de repeticão que so termina quando todas os requisitos sejam cumpridos
        senha = input('Digite uma senha: ')

        # verifica se a senha tem pelo menos 6 digitos
        if len(senha) < 6: 
            print('A senha precisa ter no mínimo 6 caracteres.')
            continue

        # Checa se tem pelo menos uma letra
        if not re.search(r'[A-Za-z1]', senha):
            print('A senha precisa ter pelo menos uma letra.')
            continue

        # Checa se tem pelo menos um caractere especial
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
            print('A senha precisa ter pelo menos um caractere especial.')
            continue

        #finaliza o laço se cumprir todos os requisitos e aceita a senha
        break

    usuarios[usuario] = senha #vincula a senha ao usuario em pares la no dicionarios
    print('Cadastro realizado com sucesso!')

def login(): # cria uma função login
    print('--- Login ---') #cria um titulo login

    
    while True: # laço de repeticão que so termina quando todas os requisitos sejam cumpridos
        usuario = input('Digite seu usuário: ')

        if usuario not in usuarios:  # verifica se o usuario ja esta no dicionario
            print('Usuário não encontrado. Tente novamente.')
        else:
            break  # sai do laço quando encontrar o usuário

    # agora ver se a senhaesta certa  com limite de 3 tentativas
    tentativas = 0 #cria uma variavel tentativa que funciona para validar as tentativas
    while tentativas > 3: # cria um laço de tentativas que quando passa de 3 incorretos ele para
        senha = input('Digite sua senha: ')

        if usuarios[usuario] == senha: #verifica se senha é digitada é igual a senha vinculada aquele usuario
            print(f'Login realizado com sucesso! Bem-vindo,{usuario}')
            return  # encerra a função
        else:
            tentativas += 1 # se senha for errada ele aumenta 1 na variavrel tentativa que antes era 0
            print(f'Senha incorreta! Você ainda tem {tentativas} tentativa(s).')

    print('Número máximo de tentativas atingido. Acesso bloqueado.') # escreve uma mensagem se o numero de tentativas chega em 3

def menu(): #cria a função menu 
    while True:
        print('----- Sistema de Login -----') #titulo da função menu
        print('1 - Cadastrar') #faz um print simples dizendo que 1 é cadastro
        print('2 - Login') #faz um print simples dizendo que 2 é o login
        print('3 - Sair') #faz um print simples dizendo que 3 é para sair
        opcao = int(input('Escolha uma opção: ')) #cira um input que so aceita os numero inteiros

        #condicional que leva as respectivas funções
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print('Saindo')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()

