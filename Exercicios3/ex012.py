print('Calculadora de Peso Ideal')
s = str(input('Insira seu sexo:')).strip().upper()
h = float(input('Insira sua altura em metros:'))
if s == 'MASCULINO':
    p = (72.7 * h) - 58
else:
    p = (62.1 * h) - 44.7
print('Seu peso ideal é {:.2f} '.format(p))
