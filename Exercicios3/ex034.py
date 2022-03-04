numero = int(input('Insira um número entre 0 e 10: '))
while not 10 >= numero >= 0:
    print('Valor inválido')
    numero = int(input('Insira um número entre 0 e 10:'))
print('Valor aceito')