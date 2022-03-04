from time import sleep
cadastro = []
usuario =[]
print('-=' * 15)
print('Programa de Cadastro de usuários')
print('-=' * 15)
while True:
    print('1- Cadastra Novo Usuário')
    print('2- Listar Usuários')
    print('3- Buscar Usuários')
    print('4- Encerrar Programa')
    print('-=' * 15)
    while True: # laço para válidar a opção
        opcao = str(input('Insira a opção desejada: ')).strip()
        if opcao in '1234':
            break
        else:
            print('Informe Opção Válida')
            print('-=' * 15)
    print('-=' * 15)
    if opcao == '1':
        nome = str(input('Insira o Nome do Usuário: ')).upper().strip()
        idade = int(input('Insira a Idade do Usuário: '))
        usuario.append(nome)
        usuario.append(idade)
        cadastro.append(usuario[:])
        usuario.clear()
    elif opcao == '2':
        for c in cadastro:
            print(f'Nome: {c[0]}      Idade: {c[1]}')
            sleep(0.7)
    elif opcao == '3':
        busca = str(input('Insira o Nome do Usuário para busca: ')).upper().strip()
        sleep(2)
        for c in range(0, (len(cadastro) - 1)):
            if busca in cadastro[c]:
                print('Usuário Encontrado')
                print(f'Nome: {cadastro[c][0]}    Idade: {cadastro[c][1]}')
                while True:
                    opcao2 = str(input('Deseja remover o usuário?[S/N] ')).strip().upper()
                    if opcao2 == 'S':
                        del(cadastro[c])
                        break
                    elif opcao2 == 'N':
                        break
                    else:
                        print('Opção Inválida!')
            else:
                print('Usuário não encontrado.')
    elif opcao == '4':
        break
    else:
        print('Erro! Opção Inválida!')
    print('-=' * 15)
print('Até Mais!')
sair = str(input('...')) # pressionar uma tecla para encerrar o programa