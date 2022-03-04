print('Cadastro de Usuário')
nome = input('Insira seu nome: ').strip()
salario = 0
while True:
    data = input('Insira sua data de aniversário (_/_/_): ').strip()
    len(data)
    if len(data) == 10:
        break
    else:
        print('Informe uma data válida!')
idade = int(input('Informe sua idade: '))
tel = input('Insira seu teleofne: ').strip()
while True:
    cpf = input('Insira seu CPF: ')
    if len(cpf) == 14 or len(cpf) == 11:
        break
    else:
        print('Informe um CPF válido!')
while True:
    rg = input('Insira seu RG: ').strip()
    if len(rg) == 9 or len(rg) == 13:
        break
    else:
        print('Informe um RG válido')
ende = input('Insira seu Endereço: ').strip()
email = input('Insira seu Email: ').strip()
while True:
    sex = input('Informe seu Sexo[F/M]: ').strip().upper()
    if sex == 'F' or sex == 'M':
        break
    else:
        print('Informe um sexo válido!')
while True:
    emp_ativo = input('Vocé é um empregado ativo [S/N]? ').strip().upper()
    if emp_ativo == 'S' or emp_ativo == 'N':
        break
    else:
        print('Siga o Padrão de resposta!')
if emp_ativo == 'S':
    salario = float(input('Informe seu salário Bruto mensal: R$ '))
    imp_renda = salario * 0.15
else:
    imp_renda = 0
print('Cadastro Efetuado com sucesso')
print('-=-' * 15)
print(f'NOME: {nome}')
print(f'Data de  Nascimento:{data}')
print(f'Idade:{idade}')
print(f'Telefone:{tel} ')
print(f'CPF: {cpf}')
print(f'RG: {rg}')
print(f'Endereço: {ende}')
print(f'Email: {email}')
print(f'Sexo: {sex}')
print(f'Empegado ativo: {emp_ativo}')
if salario > 0:
    print(f'Salário: R${salario:.2f}')
    print(f'Imposto de Renda:R${imp_renda:.2f}')
print('-=-' * 15)
