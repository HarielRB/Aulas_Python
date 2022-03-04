from time import sleep
print('Insira algumas informações abaixo')
nome = str(input('Nome: ')).strip().upper()
num_letras = len(nome)
idade = int(input('Idade: '))
salario = float(input('Salário: R$ '))
sexo = str(input('Sexo [F/M]: ')).strip().upper()
estado_civil = str(input('Estado Civil [S/C/V/D]: ')).strip().upper()
colecao_sexo = ['F', 'M']
colecao_ec = ['S', 'C', 'V', 'D']
print('ANALISANDO...')
sleep(2)
while num_letras < 3 or idade > 150 or salario <= 0 or sexo not in colecao_sexo or estado_civil not in colecao_ec:
    while num_letras < 3:
        print('NOME INVÁLIDO')
        nome = str(input('Digite seu nome novamente: ')).strip().upper()
        num_letras = len(nome)
    while idade > 150:
        print('IDADE INVÁLIDA')
        idade = int(input('Insira sua idade novamente: '))
    while salario <= 0:
        print('SALÁRIO INVÁLIDO')
        salario = float(input('Insira seu salario novamente: R$ '))
    while sexo not in colecao_sexo:
        print('SEXO INVÁLIDO')
        sexo = str(input('Insira seu sexo novamente [F/M]: ')).strip().upper()
    while estado_civil not in colecao_ec:
        print('ESTADO CIVIL INVÁLIDO')
        estado_civil = str(input('Insira seu estado civil novamente [S/C/V/D]: ')).strip().upper()
    print('ANALISANDO NOVAMENTE...')
    sleep(3)
print('REGISTRO FEITO COM SUCESSO')
