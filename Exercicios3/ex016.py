from time import  sleep
print('Calculadora de tintas empresa Y')
while True:
    print('-=-=-' * 15)
    area = float(input('Insira a área a ser pintada (valor em metros):'))
    print('-=-=-' * 15)
    print('Existem três opções a serem selecionadas:')
    print('\033[35m''Opção 1 = Apenas latas de tinta (18L).''\033[m')
    print('\033[33m''Opção 2 = Apenas galões de tintas (3,6l).''\033[m')
    print('\033[36m''Opção 3 = Galões e Latas de tintas.''\033[m')
    print('-=-=-' * 15)
    opcao = input('Insira o número da opção selecionada:').strip()
    print('-=-=-' * 15)
    while opcao not in '123':
        print('\033[1;31m''Opção inválida.''\033[m')
        opcao = input('Digite o número da opção desejada: ').strip()
    litros = area / 6
    if int(opcao) == 1:
        latas = litros // 18
        resto = litros % 18
        if resto > 0:
            print('Serão necessárias {} latas de tinta.'.format(latas + 1))
            print('O valor a ser pago é igual a R${:.2f}'.format((latas + 1) * 80))
        else:
            print('Serão necessários {:.0f} latas de tinta'.format(latas))
            print('O valor a ser pago corresponde a R${:.2f}'.format(latas * 80))
    elif int(opcao) == 2:
        latas = litros // 3.6
        resto = litros % 3.6
        if resto > 0:
            print('Serão necessários {} galões de tinta'.format(latas + 1))
            print('O valor a ser pago corresponde a R${:.2f}'.format((latas + 1) * 25))
        else:
            print('Serão necessários {:.0f} galões de tinta.'.format(latas))
            print('O valor a ser pago será de R${:.2f}'.format(latas * 25))
    elif int(opcao) == 3:
        latas = litros // 18
        resto = litros % 18
        if resto == 0:
            print('Serão necessárias {} latas de tinta e nenhum galão adicional.'.format(latas))
            print('O valor a ser pago corrsponde a R${:.2f}'.format(latas * 80))
        else:
            galoes = resto // 3.6
            resto2 = resto % 3.6
            if resto == 0:
                print('Serão necessárias {} latas de tinta e {} galões.'.format(latas, galoes))
                print('O valor a ser pago será de R${:.2f}'.format((latas * 80) + (galoes * 25)))
            else:
                print('Serão necessárias {} latas e {} galões de tinta'.format(latas, (galoes + 1)))
                print('O valor cobrado será de R${:.2f}'.format((latas * 80) + ((galoes + 1) * 25)))
    print('-=-=-' * 15)
    continuar = str(input('Deseja realizar outro processo [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print('Encerrando programa...')
sleep(2)
print('FIM DE PROCESSOS')
