s = float(input('Qual o valor do seu salario atual? R$'))
t = float(input('Qual a porcentagem de aumento?'))
n = s + (s*t/100)
print('Seu salario após o aumento será de: R$ {:.2f}'.format(n))

