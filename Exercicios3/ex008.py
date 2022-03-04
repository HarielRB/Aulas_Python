from time import sleep
print('Calculadora de salários.')
v = float(input('Valor referente a uma hora trabalhada: R$'))
h = float(input('Quantas horas você trabalha por mês:'))
print('Calculando...')
sleep(2)
print('O seu salário ao final do mês será de R${:.2f}.'.format(v * h))
