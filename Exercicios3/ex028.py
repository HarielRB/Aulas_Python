print('Calculo de folha de pagamento')
horas = float(input('Insira o total de horas trabalhadas no mês:'))
valor_hora = float(input('Insira o valor de sua hora trabalhada: R$'))
salariob = horas * valor_hora
if salariob <= 900:
    ir = 0
elif 1500 >= salariob > 900:
    ir = 0.05
elif 2500 >= salariob > 1500:
    ir = 0.10
else:
    ir = 0.20
valor_ir = ir * salariob
inss = salariob * 0.10
sind = salariob * 0.03
print('Salário bruto ( {} * {} ): R${:.2f} '.format(horas, valor_hora, salariob))
print('(-) IR ({}%): R${:.2f}'.format((ir * 100), valor_ir))
print('(-) INSS (10%): R${:.2f}'.format(inss))
print('(-) Sindicato (3%): R${:.2f}'.format(sind))
print('FGTS (11%): R${:.2f}'.format(salariob * 0.11))
desconto = valor_ir + inss + sind
print('Total de Descontos: R${:.2f}'.format(desconto))
print('Salário Líquido: R${:.2f}'.format(salariob - desconto))
