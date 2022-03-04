print('Valor Investidos em CD colecionador X')
quantidade = int(input('Insira a quantidade de cds que você possui: '))
valor_total = 0
for c in range(1, quantidade + 1):
    valor = float(input(f'Digite o valor do {c} cd: R$ '))
    valor_total += valor
    c += 1
print(f'Você gastou R${valor_total} em CDS')
media = valor_total / quantidade
print(f'A média de preço desses cds é de R${media:.2f} ')
