print('Calculadora de médias')
c = 0
# criar a variavel soma para somar o número e guarda-lo
soma = 0
for c in range(0, 5):
    c = c + 1
    num = float(input('Insira o {} número: '.format(c)))
    soma = soma + num
media = soma / c
print('A média entre esses {} valores corresponde á {}.'.format(c, media))
