print('CALCULADORA DE FATORIAL')
num = int(input('Insira o número desejado: '))
contador = num
multiplicador = 1
print('{} ! = '.format(num), end=' ')
for contador in range(num, 0, -1):
    print(' {} '.format(contador), end=' ')
    if contador > 1:
        print('X', end=' ')
    else:
        print('=', end='')
    multiplicador *= contador
    contador -= 1
print(' ', multiplicador)
print('FIM')
