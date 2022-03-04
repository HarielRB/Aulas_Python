from time import sleep
n1 = float(input('Insira um número:'))
n2 = float(input('Insira outro número:'))
n3 = float(input('Insira mais um ultimo número:'))
print('Irei te indicar qual número é o maior e qual o menor dentre os três inseridos')
print('Analisando...')
sleep(3)
m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3
ma = n3
if n1 > n3 and n1 > n2:
    ma = n1
if n2 > n3 and n2 > n1:
    ma = n2
print('O menor número é {}!'.format(m))
print('O maior número é {}'.format(ma))
print('Eu sou um gênio!')
