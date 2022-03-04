from random import randint
from time import sleep
print('-=-' * 20)
print(f'{"Sorteador de Números Mega Sena":^55}')
print('-=-' * 20)
while True:
    numeros = []
    palpites = int(input('Insira quantos palpites você deseja (999 para encerrar): '))
    if palpites == 999:
        break
    else:
        for c in range(1, palpites + 1):
            print(f'Números do jogo {c}: ', end=' ')
            sleep(1)
            for p in range(0, 6):
                aleatorio = randint(0, 60)
                while aleatorio in numeros:
                    aleatorio = randint(0, 60)
                numeros.append(aleatorio)
            numeros.sort()
            print(numeros)
            numeros.clear()
            sleep(1.5)
        print('-=-' * 20)
        print(f'{"BOA SORTE":^55}')
