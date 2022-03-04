from time import sleep
print('Conversor de ℃ para °F')
c = float(input('Insira o valor de ℃:'))
print('Calculando...')
sleep(2)
f = (c * (9/5) + 32)
print('{} ℃ corresnpondem a {:.2f} °F'.format(c, f))
