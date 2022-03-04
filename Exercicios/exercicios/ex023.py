'''n = str(input('Digite um número inteiro entre 0 e 9999:'))
print('Milhar: {}'.format(s[0]))
print('Centena:{}'.format(s[1]))
print('Dezena: {}'.format(s[2]))
print('Unidade:{}'.format(s[3]))... feito dessa maneira, o exercicio esta´ra errado,
deve ser feito por meio da maneira matematica utilizando modulo.'''

# maneira certa
n = int(input('Insira um número entre 0 e 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando seu número...')
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
