from time import sleep
print('Calculadora da área de um quadrado.')
L = float(input('Insira o valor dos lados:'))
m = str(input('Insira a unidade de medida:')).strip()
print('_' * 20)
print('Calculando...')
print('_' * 20)
sleep(2)
a = L * L
print('O valor da área do quadrado corresponde á {} {} quadrados'.format(a, m))
print('O seu dobro corresponde a {} {} quadrados'.format((a * 2), m))
