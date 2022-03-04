print('Identificador de números Primos')
# primeiro: inserir a variavel numero
num = int(input('Insira o número inteiro para análise: '))
c = 0
divisao = 0
for c in range(0, num):
    c += 1
    if num % c == 0:
        print('\033[32m''{}''\033[m'.format(c), end=' ')
        divisao += 1
    else:
        print('\033[31m''{}''\033[m'.format(c), end=' ')
if divisao == 2 or divisao == 1:
    print('\nO número {} é um número primo'.format(num))
    print('Quantidade de divisão: {}'.format(divisao))
else:
    print('\nO número {} não é um número primo'.format(num))
    print('quantidade de divisão:{}'.format(divisao))
