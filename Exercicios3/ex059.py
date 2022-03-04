print('Panificadora Pão de Ontem - Tabela de Preços')
preco = float(input('Insira o preço do Pão: R$ '))
for c in range(1, 51):
    tabela = c * preco
    print(f'{c} - R$ {tabela:.2f}')
print('Volte sempre!')
