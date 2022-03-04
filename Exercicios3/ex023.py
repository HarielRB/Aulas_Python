from time import sleep
print('Identificador de números')
num_1 = float(input('Insira o primeiro valor:'))
num_2 = float(input('Insira o segundo valor:'))
num_3 = float(input('Insira o terceiro valor:'))
print('Analisando...')
sleep(3)
m = num_1
ma = num_3
if num_1 > num_2 and num_1 > num_3:
    ma = num_1
if num_2 > num_1 and num_2 > num_3:
    ma = num_2
if num_2 < num_1 and num_2 < num_3:
    m = num_2
if num_3 < num_2 and num_3 < num_1:
    m = num_3
print('O número {} é o maior entre os três'.format(ma))
print('O número {} é o menor entre os três'.format(m))
