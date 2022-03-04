from time import sleep
print('===' * 20)
print('CHICOs STORE ')
print('===' * 20)
menor_preco = 0
contador = 0
produto_barato = ' '
soma = 0
tot_mil = 0
while True:
    produto = str(input('INSIRA O PRODUTO ADQUIRIDO: ')).strip()
    preco = float(input('INSIRA O PREÇO: R$ '))
    contador += 1
    soma += preco
    if contador == 1:
        menor_preco = preco
        produto_barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_barato = produto
    if preco > 1000:
        tot_mil += 1
    opcao = str(input('DESEJA CONTINUAR [S/N]? ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('DESEJA CONTINUAR [S/N]? ')).strip().upper()
    if opcao == 'N':
        break
print('CALCULANDO VALOR DE COMPRA.....')
sleep(3)
print('{:-^40}'.format('NOTA FISCAL'))
print(f'TOTAL A SER PAGO: R$ {soma:.2f}')
print(f'PRODUTO MAIS BARATO: {produto_barato:}')
print(f'VALOR: R$ {menor_preco:.2f}')
print(f'PRODUTOS A CIMA DE R$1000,00: {tot_mil:}')
