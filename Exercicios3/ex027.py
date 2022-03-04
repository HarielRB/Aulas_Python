print('Calculadora de aumento salarial Organizações Tabajara')
salario = float(input('Informe o valor do salário: R$'))
if salario <= 280:
    taxa = 0.20
elif 700 > salario > 280:
    taxa = 0.15
elif 1500 > salario > 700:
    taxa = 0.10
else:
    taxa = 0.05
aumento = salario * taxa
sal_novo = salario + aumento
print('Salario antes do reajuste: R% {:.2f}'.format(salario))
print('A taxa de aumento será de {}%'.format(taxa*100))
print('O valor de aumento será de R${:.2f}'.format(aumento))
print('O novo salário será de R${:.2f}'.format(sal_novo))
