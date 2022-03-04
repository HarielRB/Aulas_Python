from time import sleep
print('IDENTIFICADOR')
homens = 0
mulheres_20 = 0
maiores_de_18 = 0
while True:
    print('-=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 20)
    idade = (input('INSIRA SUA IDADE: '))
    while not idade.isnumeric():
        idade = input('INSIRA SUA IDADE: ')
    sexo = str(input('INSIRA SEU SEXO [F/M]: ')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('INSIRA SEU SEXO [F/M]: ')).strip().upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and int(idade) < 20:
        mulheres_20 += 1
    if int(idade) >= 18:
        maiores_de_18 += 1
    print('-=-' * 20)
    continuar = str(input('DESEJA CONTINUAR [S/N]? ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('DESEJA CONTINUAR [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print('REUNINDO DADOS....')
sleep(1.5)
print(f'TOTAL DE PESSOAS MAIORES DE 18 ANOS: {maiores_de_18} ')
print(f'TOTAL DE HOMENS: {homens} ')
print(f'TOTAL DE MULHERES MENORES DE 20 ANOS: {mulheres_20}')
print('Até mais')
