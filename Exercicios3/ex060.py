print('CAIXA REGISTRADORA')
while True:
    print('Lojas Tabajara')
    print('---' * 20)
    soma = 0
    c = 1
    while True:
        preco = float(input(f'Produto {c}: R$ '))
        if preco == 0:
            break
        else:
            soma += preco
            c += 1
    print(f'TOTAL: R$ {soma:.2f}')
    dinheiro = float(input('DINHEIRO: R$'))
    troco = dinheiro - soma
    print(f'TROCO: R$ {troco:.2f}')
    print('---' * 20)
