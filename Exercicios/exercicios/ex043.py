print('Calculadora de IMC')
peso = float(input('Insira seu peso em KG:'))
altura = float(input('Insira sua altura em metros:'))
imc = peso / (altura ** 2)
print('Seu IMC corresponde á {:.2f} '.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 25 > imc >= 18.5:
    print('Peso Ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 > imc >= 30:
    print('Obesidade')
else:
    print('Obesidade Morbida')
