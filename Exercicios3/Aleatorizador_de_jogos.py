from random import choice
from time import sleep
print('Aleatorizador de Jogos do Hariel')
lista = []
while True:
    lista.append(str(input('Insira um jogo: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('Hariel irei aleatorizar os seus jogos')
print('ALEATORIZANDO...')
sleep(2)
print(f'O jogo escolhido foi {choice(lista)}')
