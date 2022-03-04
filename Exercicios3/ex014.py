from time import sleep
print('Calculadora de salários e descontos')
print('Primeiro insira as seguintes informações:')
s = float(input('Valor recebido por horas trabalhadas:'))
h = float(input('Valor de horas totais no mês:'))
st = s * h
i = st * 0.08
sind = st * 0.05
ir = st * 0.11
print('Calculando...')
sleep(3)
print('O seu salário bruto equivale a R${:.2f}'.format(st))
print('São descontados os seguintes valores de seu salário bruto')
print('INSS: R$ {}'.format(i))
print('Sindicato: R${:.2f}'.format(sind))
print('Imposto de Renda: R${:.2f}'.format(ir))
print('O valor de seu salário líquido corresponde a:')
print('R${:.2f}'.format(st - i - sind - ir))
