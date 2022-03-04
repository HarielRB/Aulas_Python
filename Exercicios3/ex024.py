print('Identificador de preços')
preco_1 = float(input('Insira o valor do primeiro produto: R$'))
preco_2 = float(input('Insira o valor do segundo produto: R$'))
preco_3 = float(input('Insira o valor do terceiro produto: R$'))
menor = preco_1
if preco_2 < preco_1 and preco_2 < preco_3:
    menor = preco_2
if preco_3 < preco_2 and preco_3 < preco_1:
    menor = preco_3
print('O produto com valor de R${} possui o menor valor, ele é quem deve ser comprado.'.format(menor))
