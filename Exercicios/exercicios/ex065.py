from time import sleep
print('Calculadora de médias')
num = 0
divisor = 0
opcao = 'S'
menor_nota = 0
maior_nota = 0
soma = 0
while opcao != 'N':
    num = int(input('Insira um número: '))
    soma = soma + num
    opcao = str(input('Gostaria de adicionar mais um número [S/N]? ')).strip().upper()
    divisor = divisor + 1
    if opcao != 'S' and opcao != 'N':
        print('Opção invalida')
    if divisor == 1:
        maior_nota = num
        menor_nota = num
    elif num > menor_nota:
        maior_nota = num
    elif num < menor_nota:
        menor_nota = num
print('\033[1;35m''CALCULANDO...''\033[m')
sleep(2)
print('A média desses {} valores corresponde á {:.2f}'.format(divisor, soma / divisor))
if maior_nota == menor_nota:
    print('Os número digitados são iguais')
else:
    print('O maior número apresentado foi {}'.format(maior_nota))
    print('o Menor número apresentado foi {}'.format(menor_nota))
