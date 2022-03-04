from time import sleep
print('---' * 15)
print('Identificador de condição de existência de um triângulo')
print('---' * 15)
sleep(2)
a = float(input('Insira o comprimento da reta um:'))
b = float(input('Insira o comprimento da reta dois:'))
c = float(input('Insira o comprimento da reta três:'))
print('Analisando...')
sleep(3)
if a < b + c and b < a + c and c < a + b:
    print('Há a possibilidade de contruir um trângulo com essas retas')
else:
    print('Não Há possibilidade de contruir um triângulo com essas retas.')

# utilize o and quando for necessário mais de uma variavel
