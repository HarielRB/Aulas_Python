from time import sleep
print('-=-' * 20)
print('ANALISADOR DE EXISTENCIA DE TRIANGULOS')
print('-=-' * 20)
sleep(1)
a = float(input('Insira o valor do primeiro lado:'))
b = float(input('Insira o valor do segundo lado:'))
c = float(input('Insira o valor do terceiro lado:'))
print('\033[1;35m''ANALISANDO...''\033[m')
sleep(3)
if a < b + c and b < c + a and c < a + b:
    print('\033[1;34m''Há a possibilidade de se construir um triângulo com essas medidas''\033[m')
    print('Agora analisaremos o tipo de triângulo que pode ser construido')
    print('\033[1;35m''IDENTIFICANDO TIPO...''\033[m')
    sleep(3)
    if a == b and b == c and c == a:
        # Pode ser escrito como: a == b == c:
        tipo = '\033[1;33m''Triângulo Equilátero''\033[m'
    elif a == b or b == c or c == a:
        tipo = '\033[1;36m''Triângulo Isóceles''\033[m'
    else:
        tipo = '\033[1;32m''Triângulo Escaleno''\033[m'
    print('O seu triângulo é um {}.'.format(tipo))
else:
    print('\033[1;31m''Não Há a possibilidade de se construir um triangulo.''\033[m')
