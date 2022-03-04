from time import sleep
"""print('Identificador de números primos:')
numero = int(input('Insira um número inteiro: '))
print('IDENTIFICANDO...')
sleep(2)"""
# Busquei ajuda nos videos de resolução
# Resolução:
# primeiro devemos pedir para o usuário inserir um número
numero = int(input('Insira um número inteiro: '))
# criaremos agora uma variavel para o calculo ao final
divisores = 0
# Agora utilizaremos os laços com o for
for c in range(1, numero + 1):
    # adicionaremos agora uma condição
    if numero % c == 0:
        print('\033[34m', end=' ')
        divisores = divisores + 1
    else:
        print('\033[31m', end=' ')
    # agora devemos printar o c
    print('{}'.format(c), end=' ')
print('\n\033[mO numero foi dividido {} vezes'.format(divisores))
# ja podemos identificar agora se o número é primo ou não
# agora criaremos a seguinte condição
if divisores == 2 or divisores == 1:
    # um número primo só é divisivel duas vezes, sendo elas por 1 e pelo próprio número
    print('O número {} é Primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))
