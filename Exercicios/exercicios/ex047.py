from time import sleep
print('Apresentator de Número pares entre 1 e 50:')
for c in range(2, 51, 2):
    # utilizar o end = ' ' no final para printar tudo em uma linha
    # caso eu nao utlizie o tercei número ali, o pc vai rodar todos eles sem pular de 2 em 2
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.5)
print('.')
print('Esses são os todos os números pares.')
