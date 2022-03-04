numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
          'Treze', 'Catorze', 'Quinze', 'Dezeseis', 'Desesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = input('Digite um número entre 0 e 20 (SAIR PARA ENCERRAR): ').strip().upper()
    if num == 'SAIR':
        break
    while not 20 >= int(num) >= 0:
        print('\033[1;31m''NÚMERO INVÁLIDO''\033[m')
        num = input('Digite novamente um número entre 0 e 20 (SAIR PARA ENCERRAR): ')
    print(f'Voce digitou o número {numero[int(num)]}')
print('Até mais')
