print('Cadastro empresa X')
nome = str(input('Insira seu nome de usuário: ')).strip().upper()
senha = str(input('Insira sua senha: ')).strip().upper()
while nome == senha:
    print('A senha não pode ser igual ao nome')
    senha = str(input('Insira uma senha diferente: ')).strip().upper()
print('Senha aceita')