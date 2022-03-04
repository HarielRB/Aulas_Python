print('-=-' * 20)
print('{:^50}'.format('ISHUZOKU BANCO'))
print('-=-' * 20)
valor_saque = int(input('Insira o valor desejado para saque: R$'))
print('====' * 20)
nota_50 = valor_saque // 50
print(f'Notas de R$50,00: {nota_50}')
nota_20 = valor_saque % 50 // 20
if nota_20 > 0:
    print(f'Notas de R$20,00: {nota_20}')
nota_10 = valor_saque % 50 % 20 // 10
if nota_10 > 0:
    print(f'Notas de R$10,00: {nota_10}')
nota_1 = valor_saque % 50 % 20 % 10 // 1
if nota_1 > 0:
    print(f'Notas de R$1,00: {nota_1}')
