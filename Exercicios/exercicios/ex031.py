print('Calcularemos o valor da sua viagem!')
k = float(input('Insira o Valor da quilometragem:KM'))
if k <= 200:
    p1 = k * 0.50
else:
    p1 = k * 0.45
print('O valor da sua viagem será de: R$ {:.2f}'.format(p1))
print('Tenha uma boa viagem!')
