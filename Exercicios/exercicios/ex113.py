def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31m''Erro, digite apenas números inteiros''\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida')
            return 0
        else:
            return n


def leia_float(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31m''Erro, digite apenas números reais''\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida')
            return 0
        else:
            return n


inteiro = leia_int('Digite um número Inteiro: ')
real = leia_float('Digite um número Real: ')
print(f'O número Inteiro digitado foi {inteiro} e o número Real foi {real} ')
