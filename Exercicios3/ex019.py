from time import sleep
num = float(input('Insira um número:'))
print('Analisando....')
sleep(3)
if num > 0:
    print('O número {} é positivo.'.format(num))
else:
    print('O número {} é negativo.'.format(num))
