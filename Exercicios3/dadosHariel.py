from time import sleep
import random
print('Lançador de dados do Hariel')
print('Opção 1: D4')
print('Opção 2: D6')
print('Opção 3: D8')
print('Opção 4: D10')
print('Opção 5: D20')
print('Opção 6: D100')
while True:
    dado = input('Insira o NÚMERO da opção desejada (digite sair para encerrar): ').strip().upper()
    if dado == 'SAIR':
        print('OK')
        break
    else:
        print('\033[1;35m''ARREMESSANDO DADO...''\033[m')
        sleep(2)
        if int(dado) == 1:
            print('Você arremessou um D4 e caiu')
            print(random.randint(1, 4))
        elif int(dado) == 2:
            print('Você arremessou um D6 e caiu')
            print(random.randint(1, 6))
        elif int(dado) == 3:
            print('Você arremessou um D8 e caiu')
            print(random.randint(1, 8))
        elif int(dado) == 4:
            print('Você arremessou um D10 e caiu')
            print(random.randint(1, 10))
        elif int(dado) == 5:
            print('Você arremessou um D20 e caiu')
            print(random.randint(1, 20))
        elif int(dado) == 6:
            print('Você arremessou um D100 e caiu')
            print(random.randint(0, 100))
        else:
            print('\033[1;31m''opção invalida''\033[m')
print('Até mais.')
input('...')
