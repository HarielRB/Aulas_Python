from time import sleep
print('Sistema para aprovação de Empréstimos')
vcasa = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira seu salário bruto: R$'))
ano = int(input('Insira o tempo, em anos, para efetuar o pagamento:'))
prestacao = vcasa / (ano * 12)
print('\033[1;32m''Calculando...''\033[m')
sleep(2)
print('O valor da prestação será de R$ {:.2f}'.format(prestacao))
porc = salario * 0.30
if prestacao > porc:
    print('\033[31m''Infelizmente seu empréstimo foi negado.''\033[m')
else:
    print('\033[34m''Seu empréstimo foi aprovado.''\033[m')
