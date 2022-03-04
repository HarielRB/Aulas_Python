colecao = ['M', 'F']
sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in colecao:
    # while sexo not in 'MmFf':
    print('\033[1;31m''Sexo inválido''\033[m')
    sexo = str(input('Insira seu sexo [M/F]:  ')).strip().upper()[0]
print('\033[1;33m''Validação aceita''\033[m')
