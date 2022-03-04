import random
from time import sleep
n = 1
print('\033[34m''-=-' * 20)
print('\033[33m''JOGO DA ADIVINHAÇÂO 2.0')
print('\033[34m''-=-''\033[m' * 20)
print('O computador irá pensar em um número entre 0 e 10')
print('\033[35m''PENSANDO....''\033[m')
sleep(2)
num_pc = random.randint(0, 10)
num_jogador = int(input('Em qual número eu pensei jogador? '))
while num_jogador != num_pc:
    print('\033[1;31m''Você errou''\033[m')
    # num_jogador = int(input('Tente de novo jogador: '))
    n = n + 1
    if num_jogador > num_pc:
        num_jogador = int(input('Tente com um numero menor jogador...'))
    else:
        num_jogador = int(input('Tente um número maior jogador: '))
print('Você' '\033[1;32m'' ACERTOU ''\033[m''jogador o número {} foi o qual pensei'.format(num_pc))
print('Você precisou de {} paplpites para acertar'.format(n))
