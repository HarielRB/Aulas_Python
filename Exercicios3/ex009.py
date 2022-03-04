from time import sleep
print('Conversor de graus F para C')
f = float(input('Insira a temperatura em °F:'))
print('Convertendo...')
sleep(2)
c = (5 * (f-32)/9)
print('{} °F correspondem á {:.2f} ℃'.format(f, c))
