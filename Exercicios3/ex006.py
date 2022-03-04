from time import sleep
print('Calculadora da área de um Círculo')
r = float(input('Insira o valor do Raio:'))
um = str(input('insira a unidade de medidas:')).strip()
print('_' * 20)
print('Calculando...')
print('_' * 20)
sleep(2)
print('Um circulo com raio igual á {} {} possui uma área correspondete á {:.2f} {} quadrados'
      .format(r, um, (3.14 * (r ** 2)), um))
print('Obrigado pela preferência!')
