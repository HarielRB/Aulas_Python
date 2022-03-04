from time import sleep


def contador(i, f, p):
    for c in range(i, f + 1, p):
        print(c, end=' ')
        sleep(0.5)
    print('FIM !')


def linha(txt):
    print('~' * (len(txt) + 1))
    print(txt)
    print('~' * (len(txt) + 1))


linha('Contador de 1 até 10:')
contador(1, 10, 1)
linha('Contador de 10 até 0 pulando de 2 em 2:')
contador(10, 0, -2)
linha('Agora é sua vez de personalizar: ')
while True:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if fim < inicio:
        passo *= -1
    elif passo == 0:
        passo = 1
    contador(inicio, fim, passo)
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('Até mais!!!')
