print('Calculadora de descontos)')
p = float(input('Qual o valor do produto sem descontos?'))
t = float(input('Qual a porcentagem do desconto (apenas o número):'))
tr = t/100
print('O valor do produto com o desconto será de R$ {:.2f}'.format(p-(p*tr)))
