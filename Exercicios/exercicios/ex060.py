# Utilizando FOR pois existe um limite
"""print('Calculadora de fatorial')
numero = int(input('Insira o número para o calculo de seu fatorial: '))
multiplicacao = 1
for c in range(numero, 0, -1):
    print(' {} '.format(c), end='X')
    multiplicacao = multiplicacao * c
print('\n''{}! corresponde á {} '.format(numero, multiplicacao))"""

# Utilizando while
numero = int(input('Insira um número: '))
c = numero
multiplicacao = 1
print('Calculando {} ! = '.format(numero), end= '')
while c > 0:
    print(' {} '.format(c), end='')
    if c > 1:
        print('x', end='')
    else:
        print('=', end='')
    # a multiplicação deve vir antes da variavel c e sua mudança
    multiplicacao = multiplicacao * c
    c = c - 1
print(' {}'.format(multiplicacao))