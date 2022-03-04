# envolve bases numericas, consultar video resposta e o curso referente a bases numericas
print('Converso de bases numericas')
numero = int(input('Insira um numero inteiro:'))
print('Vou te dar algumas opções de transformação:')
print('\033[32m''Opção 1: Binário''\033[m')
print('\033[33m''Opção 2: Octal''\033[m')
print('\033[34m''Opção 3: Hexadecimal''\033[m')
opcao = int(input('Insira sua opção:'))
if opcao == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[1;31m''Opção Inválida''\033[m')
