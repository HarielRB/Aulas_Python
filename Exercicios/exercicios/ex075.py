num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite mais um número: '))
num_4 = int(input('Digite o ultimo número: '))
# podemos colocar os valores direto em uma tulpa
# num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
# int(input('Digite um número: ')))
conjunto = (num_1, num_2, num_3, num_4)
print(f'Apariçoes do número 9: {conjunto.count(9)}')
if 3 not in conjunto:
    print('O valor 3 não foi digitado')
else:
    print(f'O valor 3 apareceu na {conjunto.index(3) + 1}ª posição pela primeira vez')
print('Números pares: ', end=' ')
for c in conjunto:
    if c % 2 == 0:
        print(c, end=' ')
