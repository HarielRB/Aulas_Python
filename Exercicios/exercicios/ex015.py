print('Calculadora para o valor final de alugueis de carro')
km = float(input('Quantos quilometros foram percorridos com o carro?'))
d = int(input('Quantos dias o carro ficou em uso?'))
km2 = 0.15 * km
d2 = 60 * d
t = km2 + d2
print('O valor total do aluguel do carro corresponde a R{:.2f}'.format(t))
