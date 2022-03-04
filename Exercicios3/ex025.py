n1 = float(input('Insira um número:'))
n2 = float(input('Insira o segundo número:'))
n3 = float(input('Insira o terceiro número:'))
ma = n1
m = n2
me = n3
if n2 > n3 and n2 > n1:
    ma = n2
if n3 > n2 and n3 > n1:
    ma = n3
if n2 < n1 and n2 < n3:
    me = n2
if n1 < n2 and n1 < n3:
    me = n1
if n1 > n3 > n2 or n2 > n3 > n1:
    m = n3
if n2 > n1 > n3 or n3 > n1 > n2:
    m = n1
print('A ordem decrescente deses valores é igual a: {}; {}; {}.'.format(ma, m, me))
