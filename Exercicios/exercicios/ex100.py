from random import randint
from time import sleep


def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    c = 0
    s = 0
    for valores in lista:
        if valores % 2 == 0:
            s += valores
        c += 1
    print(f'A soma dos numeros pares corresponde á {s}')


# programa principal
numeros = list()
print('Aleatorizando números...')
sleep(1)
sorteio(numeros)
print(numeros)
sleep(0.5)
somapar(numeros)
