from time import sleep
print('Gerenciador de pagamentos Diferencial Saúde.')
preco = float(input('Insira o Valor do produto: R$'))
print('Selecione uma das opções de pagamento:')
print('\033[34m''Opção 1: A vista em cheque ou dinherio')
print('\033[33m''Opção 2: A vista no cartão')
print('\033[35m''Opção 3: em até 2X no cartão')
print('\033[36m''Opção 4: 3X ou mais no cartão''\033[m')
opcao = int(input('Insira a opção desejada:'))
print('\033[1;34m''CALCULANDO...''\033[m')
sleep(3)
if opcao == 1:
    valor = preco - (preco * 0.10)
    print('O valor a ser pago será de R$ {:.2f}'.format(valor))
    # desconto de 10%
elif opcao == 2:
    valor = preco - (preco * 0.05)
    print('O valor a ser pago será de R${:.2f}'.format(valor))
    # desconto de 5%
elif opcao == 3:
    valor = preco
    parcelas = preco / 2
    print('O valor das parcelas será de R$ {:.2f}'.format(parcelas))
    # não há descontos
elif opcao == 4:
    valor = preco + (preco * 0.20)
    # há o acressimo de 20% do valor total no preço
    num_p = int(input('Insira a quantidade de parcelas desejadas: '))
    parcelas = valor / num_p
    print('O valor da compra será R${:.2f} com JUROS'.format(valor))
    print('O valor das parcelas será de R${:.2f}'.format(parcelas))
else:
    print('\033[1;31m''OPÇÂO INVÀLIDA''\033[m')
