import math
h = float(input('Digite um número com decimais e eu te direi sua parte inteira:'))
i = math.trunc(h)
print('A parte inteira de {} corresponde ao número {}'.format(h, i))

'''Pode ser resolvido dessa maneira:
n = float(input('Digite um numero'))
print('Você digitou o número {} e sua parte inteira corresponde a {}'.format(n, int(n))'''
