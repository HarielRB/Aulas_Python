from datetime import date

print('Será que seu ano é bissexto ?')
a = int(input('Insira o seu ano (insira 0 para analisar o ano atual):'))
if a == 0:
    a = date.today().year
elif a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    # O sinal de ! foi utilizado para representar diferença
    print('O ano {} é Bissexto'.format(a))
    # o ano bissesto não pode ser divisivel por 100 e deve ser divisivel por 400
else:
    print('O ano {} não é Bissexto'.format(a))
print('É isso ai cara!!!')
