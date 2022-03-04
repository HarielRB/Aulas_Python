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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha)
    opc = leia_int('Sua Opção: ')
    return opc
