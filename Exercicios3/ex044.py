from time import sleep
print('-=-' * 20)
print('PROGRAMA TABUADA')
print('-=-' * 20)
c = 0
num = int(input('Insira o número desejado: '))
print('CALCULANDO...')
sleep(1.5)
print('~' * 30)
for c in range(1, 11):
    print('{} X {} = {} '.format(num, c, (num * c)))
    c = c + 1
print('~' * 30)
print('Até mais')