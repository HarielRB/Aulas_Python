from time import sleep
print('Tabuada versão 2.0')
numero = float(input('Insira o número que você gostaria de saber a tabuada: '))
print('CALCULANDO...')
sleep(3)
for c in range(1, 11):
    # pode ser escrito tbm da seguinte maneira
    # print(' {} X {} = {:.2f}'.format(numero, c, c * numero))
    tab = numero * c
    print(' {} X {} = {:.2f} '.format(numero, c, tab))
opcao = str(input('Faltou alguma multiplicação? ')).strip().upper()
if opcao == 'SIM':
    print('OK!')
    mult = float(input('Insira o multiplicador desejado:'))
    print('CALCULANDO...')
    sleep(2)
    print('O resultado dessa multiplicação é {}'.format(mult * numero))
else:
    print('Até mais então !!!!')
