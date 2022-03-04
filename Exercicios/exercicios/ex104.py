def leiaint(txt):
    """--> Função para ler algo digitado e valida-lo caso seja um número
    :parametro txt: recebe o valor digitado pelo teclado
    return: retorna o número digitado de forma inteira"""
    while True:
        numero = input(txt)
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[1;31m''Erro, digite apenas números inteiros''\033[m')
    return numero


while True:
    n = leiaint('Digite um número: ')
    print(f'Foi digitado o número {n}')
