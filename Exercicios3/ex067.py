from time import sleep
print('--' * 25)
print(f'{"Lanchonete Katapimba":^40}')
print('--' * 25)
total = 0
comida = ('Cachorro Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hambúrguer', 'Cheese Burguer', 'Batata Frita G',
          'Refrigerante')
codigo = (100, 101, 102, 103, 104, 105, 106)
preco = (1.20, 1.30, 1.50, 1.20, 1.30, 10.00, 1.00)
while True:
    print(f'{"Especificações":^10}{"Código":^20}{"Preço":^10}')
    for c in range(0, 7):
        print(f'{comida[c]:15}{codigo[c]:.^20}R${preco[c]:^10.2f}')
    print('-=' * 25)
    pedido = []
    while True:
        consumo = int(input('Digite o código do produto desejado: '))
        while consumo not in codigo:
            print('Código inválido')
            consumo = int(input('Digite o código do produto desejado: '))
        quantidade = int(input('Insira sua quantidade: '))
        print('--' * 25)
        if consumo == 100 or consumo == 103:
            valor = 1.20 * quantidade
            if consumo == 100:
                pedido.append(['Cachorro Quente', quantidade, valor])
            else:
                pedido.append(['Hambúrguer', quantidade, valor])
        elif consumo == 101 or consumo == 104:
            valor = 1.30 * quantidade
            if consumo == 101:
                pedido.append(['Bauru Simples', quantidade, valor])
            else:
                pedido.append(['CHeese Burguers', quantidade, valor])
        elif consumo == 102:
            valor = 1.50 * quantidade
            pedido.append(['Bauru com Ovo', quantidade, valor])
        elif consumo == 105:
            valor = 10.00 * quantidade
            pedido.append(['Batata Frita G', quantidade, valor])
        else:
            valor = 1 * quantidade
            pedido.append(['Refrigerante', quantidade, valor])
        total += valor
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar == 'N':
            break
    print('Finalizando pedido....')
    sleep(1.5)
    print(f'{"No.":^4}{"PRODUTO":.<25}{"Quantidade":.^25}{"Valor Total":.>25}')
    for indice, elemento in enumerate(pedido):
        print(f'{indice:^4}{elemento[0]:.<25}{elemento[1]:.^25}{elemento[2]:.>25.2f}')
    print('-' * 79)
    print(f'{"VALOR TOTAL:":<4}{total:.>67.2f}')
    sleep(3)
    print('Siga para o caixa mais próximo')
    sleep(2)
    tecla = input()
    opcao = str(input('Deseja fazer um pedido? [S/N] ')).strip().upper()
    while opcao not in 'SsNn':
        opcao = str(input('Deseja fazer um pedido ? [S/N] ')).strip().upper()
    if opcao in 'Nn':
        break
print('ENCERRANDO SISTEMA...')
sleep(5)
print('SISTEMA ENCERRADO')
