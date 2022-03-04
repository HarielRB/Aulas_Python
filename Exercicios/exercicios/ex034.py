print('Calculadora de aumento Salarial!!')
s = float(input('Insira o valor de seu salário: R$'))
if s > 1250.00:
    s1 = s * 0.10
else:
    s1 = s * 0.15
print('Seu aumento será de R$ {}'.format(s1))
print('Seu novo salário será de R$ {}'.format(s + s1))
