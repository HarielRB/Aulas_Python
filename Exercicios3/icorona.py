rosario = [{'Medicamento': 'Dipirona', 'Preço': 10.00}, {'Medicamento': 'Neusaudina', 'Preço': 3.50}]
raia = [{'Medicamento': 'Nimesulida', 'Preço': 45.00}, {'Medicamento': 'Loratadina', 'Preço': 12.50}]
farmacias_regiao = ('rosario', 'raia')
lista = []
while True:
    while True:
        farmacia = str(input('Qual farmacia você deseja efetuar a compra de seus medicamentos ? ')).strip().lower()
        if farmacia in farmacias_regiao:
            break
        else:
            print('Opção Inválida, por favor digite corretamente')
    if farmacia == 'rosario':
        lista.append(rosario[:])
    elif farmacia == 'raia':
        lista.append(raia[:])
    for f in lista:
        for m in f:
            for v in m.values():
                print(f'{v:<15}', end=' ')
                print()
    pedido = []
    total = 0
    while True:
        remedio = str(input('Digite o medicamento desejado: ')).strip().capitalize()
        for f in lista:
            for m in f:
                if remedio == m['Medicamento']:
                    pedido.append(m.copy())
        for p in pedido:
            if remedio == p['Medicamento']:
                while True:
                    quantidade = input('Insira a quantidade desejada: ')
                    if quantidade.isnumeric():
                        break
                    else:
                        print('Por favor digite números')
                p['Quantidade'] = int(quantidade)
                preco_remedio = int(quantidade) * p['Preço']
                p['Total Compra'] = preco_remedio
                total += preco_remedio
        while True:
            continuar = str(input('Deseja fazer outro pedido? [S/N] ')).strip().upper()
            if continuar in 'SN':
                break
        if continuar in 'N':
            break
    print('FINALIZANDO PEDIDO...')
    for c in pedido:
        print(f'{c["Medicamento"]:.<15}{c["Quantidade"]:.^15}{c["Total Compra"]:.>15.2f}')
    print(f'Total {total:.>39.2f}')
