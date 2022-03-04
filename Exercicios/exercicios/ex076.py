print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
listagem = ('Celular', 1500.50, 'Notbook', 2650, 'Teclado', 350.50, 'Mouse', 250, 'Tablet', 650)
# print(listagem[0], '....' * 5, 'R$', listagem[1])
# print(listagem[2], '....' * 5, 'R$', listagem[3])
tamanho = len(listagem)
for c in range(0, tamanho, 2):
    if c <= tamanho:
        ordem_1 = listagem[c]
        ordem_2 = listagem[c + 1]
        print(f'{ordem_1:.<30} R$ {ordem_2:>7.2f}')
