cadastro = [['HARIEL', 22], ['HARIANNE', 20], ['MATHEUS', 23]]


def buscar(nome):
    for c in range(0, len(cadastro)):
        if cadastro[c][0] == nome:
            print(f'Nome: {cadastro[c][0]}     Idade: {cadastro[c][1]}')


def remover(nome):
    for c in range(0, len(cadastro)):
        if cadastro[c][0] == nome:
            del(c)
    return cadastro


usuario = str(input('Insira o nome do usuário: ')).strip().upper()
buscar(usuario)
opcao = str(input('Deseja remover usuário ? [S/N] ')).strip().upper()
if opcao == 'S':
    cadastro = remover(usuario)
print(cadastro)
