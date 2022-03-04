from time import sleep
print('Resolverei a soma de dois número')
n1 = float(input('Insira o primeiro valor:'))
n2 = float(input('Insira o segundo valor:'))
print('-'*20)
print('Calculando...')
print('-'*20)
sleep(4)
print('O resultado da soma entre {} e {} é igual a {}'.format(n1, n2, (n1 + n2)))
