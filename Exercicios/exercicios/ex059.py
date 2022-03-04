print('Calculadora de operações básicas')
operacao = '0'
num_1 = float(input('insira o primeiro número: '))
num_2 = float(input('Insira o segundo número: '))
while operacao != '5':
    print('Qual operação você deseja realizar?')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Inserir novos número')
    print('[ 5 ] Sair do programa')
    operacao = str(input('Insira o número da opção desejada: '))
    if operacao == '1':
        soma = num_1 + num_2
        print('A soma corresponde a {:.2f}'.format(soma))
    elif operacao == '2':
        multiplicar = num_1 * num_2
        print('A multiplicação corresponde a {:.2f}'.format(multiplicar))
    elif operacao == '3':
        if num_1 > num_2:
            print('O número {} é o maior dentre os dois'.format(num_1))
        else:
            print('O número {} é o maior dentre os dois'.format(num_2))
    elif operacao == '4':
            num_1 = float(input('Insira o primeiro número: '))
            num_2 = float(input('Insira o segundo número: '))
    else:
        print('Opção Inválida')
print('Até mais')