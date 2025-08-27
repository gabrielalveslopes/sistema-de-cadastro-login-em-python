import re   # importa o módulo "re", usado para trabalhar com expressões regulares (vai ajudar a validar a senha)

usuarios = {
    "admin1": {"senha": "123456a.", "perfil": "admin"}
}


# função para cadastrar um novo usuário
def cadastrar():
    print('--- Cadastro ---')   # título da seção no console
    usuario = input('Digite um nome de usuário: ')   # pede o nome do usuário
    
    if usuario in usuarios:   # verifica se esse nome já existe no dicionário
        print('Usuário já existe! Tente outro.')   # avisa que não pode repetir
        return   # sai da função sem cadastrar
    
    while True:   # laço para garantir que a senha seja válida
        senha = input('Digite uma senha: ')   # pede a senha

        if len(senha) < 6:   # verifica se a senha tem menos de 6 caracteres
            print('A senha precisa ter no mínimo 6 caracteres.')
            continue   # volta para pedir de novo

        if not re.search(r'[A-Za-z]', senha):   # verifica se não tem nenhuma letra
            print('A senha precisa ter pelo menos uma letra.')
            continue

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):   # verifica se não tem caractere especial
            print('A senha precisa ter pelo menos um caractere especial.')
            continue

        break   # se passou em todas as verificações, sai do laço

    usuarios[usuario] = {
    "senha": senha,
    "perfil": "comum"
}
    print('Cadastro realizado com sucesso!')   # confirma o cadastro

# função de login
def login():
    print('--- Login ---')

    usuario = input('Digite seu usuário: ').strip()  # pede só uma vez
   
    if usuario not in usuarios:   # se não existir no dicionário
        print('Usuário não encontrado. Voltando ao menu...')
        return   # volta pro menu sem entrar na parte de senha


    tentativas = 0   # contador de tentativas
    while tentativas < 3:   # só permite 3 tentativas
        senha = input('Digite sua senha: ')

        if usuarios[usuario]['senha'] == senha:   # compara a senha digitada com a cadastrada
            print(f'Login realizado com sucesso! Bem-vindo, {usuario}')
            if usuario == "admin1":
             for nome in usuarios:
                print("nome:", nome,"senha:",senha)
                                
            return   # sai da função se logar certo
                    
        
        else:
            tentativas += 1   # aumenta o número de tentativas
            print(f'Senha incorreta! Você ainda tem {3 - tentativas} tentativa(s).')

    print('Número máximo de tentativas atingido. Acesso bloqueado.')   # se errar 3 vezes, bloqueia

# função para excluir um usuário
def excluir_usuario():
    print('--- Excluir Usuário ---')
    usuario = input('Digite o nome do usuário que deseja excluir: ')   # pede o nome a excluir
    
    if usuario in usuarios:   # verifica se existe
        confirmacao = input(f'Tem certeza que deseja excluir o usuário "{usuario}"? (s/n): ')
        if confirmacao.lower() == 's':   # se digitar "s", confirma exclusão
            del usuarios[usuario]   # apaga o usuário do dicionário
            print(f'Usuário "{usuario}" excluído com sucesso!')
        else:
            print('Exclusão cancelada.')   # se não confirmar, não exclui
    else:
        print('Usuário não encontrado.')   # caso o nome não esteja cadastrado
        return

# função principal com o menu
def menu():
    while True:   # laço para manter o menu rodando até a pessoa escolher sair
        print('----- Sistema de Login -----')
        print('1 - Cadastrar')
        print('2 - Login')
        print('3 - Excluir Usuário')
        print('4 - Sair')
        try:
            opcao = int(input('Escolha uma opção: '))   # pede a opção
        except ValueError:   # se digitar algo que não é número
            print("Digite apenas números!")
            continue   # volta para pedir de novo

        if opcao == 1:   # se escolher 1
            cadastrar()
        elif opcao == 2:   # se escolher 2
            login()
        elif opcao == 3:   # se escolher 3
            excluir_usuario()
        elif opcao == 4:   # se escolher 4
            print('Saindo')   # encerra o programa
            break
        else:
            print('Opção inválida. Tente novamente.')   # se digitar algo fora de 1-4


menu()   # chama a função menu() para começar o programa
