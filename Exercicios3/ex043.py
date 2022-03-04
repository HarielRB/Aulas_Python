print('Sequencia de X até Y')
num_1 = int(input('Insira o início da sequência: '))
num_2 = int(input('Insira o término da sequência: '))
soma = 0
c = 0
for c in range(num_1, num_2 + 1):
    print(c, end=' → ')
    soma = soma + c
print('a Soma desses {} termos corresponde á {}'.format(c, soma))
