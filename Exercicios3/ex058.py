print('-=-' * 20)
print('Lojas Quase Dois - Tabela de Preço')
print('-=-' * 20)
quantidade = int(input('Insira a quantidade de produtos comprada pelo cliente: '))
for c in range(1, quantidade + 1):
    valor = c * 1.99
    print(f'{c} - R${valor:.2f}')
    c += 1
print('OBRIGADO E VOLTE SEMPRE')
