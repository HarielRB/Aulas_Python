print('CALCULADORA DE PARCELAS')
while True:
    divida = float(input('Insira o valor da divida: R$ '))
    taxa = 0.10
    print(f'{"Valor da divida":^20}{"Valor dos juros":^20}{"Quantidade de parcelas":^20}{"Valor das Parcelas":^20}')
    for c in range(1, 13):
        if c == 1:
            print(f'{divida:^20}{0:^20}{c:^20}{divida:^20}')
        elif c % 3 == 0:
            juros = taxa * divida
            parcela = (juros + divida) / c
            print(f"{divida + juros:^20}{juros:^20.2f}{c:^20}{parcela:^20.2f}")
            taxa = taxa + 0.05
    continuar = str(input('Deseja continuar ?[S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('PROGRAMA ENCERRADO')
