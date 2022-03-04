print('Conversor de metros para centimetro!')
m = float(input('Insira a metragem a ser convertida:'))
print('~' * 20)
print('Convertendo')
print('~' * 20)
from time import sleep
sleep(3)
print('{} metros correspondem á {:.2f} centimetros. '.format(m, (m * 100)))
