print('Calculadora do Valor Futuro')
valor_presente = float(input('Digite o Valor Presente: R$ '))
taxa_porcentagem = float(input('Digite o Valor da Taxa [%]:  '))
taxa_real = taxa_porcentagem / 100
n = int(input('Informe o número de prestações: '))
for c in range(1, n + 1):
    valor_parcela = valor_presente + (valor_presente * taxa_real)
    valor_presente = valor_parcela
    print(f'Parcela {c}: R${valor_presente:.2f}')
print('Essas serão suas párcelas')
