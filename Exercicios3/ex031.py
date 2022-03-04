from math import sqrt
from time import sleep
print('\033[34m''-=-''\033[m' * 20)
print('\033[1;32m''CALCULADORA DE EQUAÇÔES ')
print('\033[34m''-=-''\033[m' * 20)
a = float(input('Insira o valor de A: '))
if a == 0:
    print('Equação do primeiro grau')
else:
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))
    print('{}X2 + {}X + {} = 0 '.format(a, b, c))
    delta = (b ** 2) - 4 * a * c
    print('\033[1;35m''CALCULANDO...''\033[m')
    sleep(3.5)
    print(delta)
    if delta < 0:
        print('A equação possui solução vazia')
    elif delta == 0:
        deltan = sqrt(delta)
        x = ((b * -1) + deltan) / (2 * a)
        print('A equação apresenta apenas uma raiz como solução')
        print('S = [ {} ]'.format(x))
    else:
        deltan = sqrt(delta)
        x1 = ((b * -1) + deltan) / (2 * a)
        x2 = ((b * -1) - deltan) / (2 * a)
        print('A equação apresenta duas raízes sendo elas:')
        print('S = [ {:.2f} ; {:.2f}'.format(x1, x2))
