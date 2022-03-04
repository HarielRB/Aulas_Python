import random
from time import sleep

print('Vamos fazer um jogo de adivinhação!')
print('Vou pensar em um número entre 0 e 5, tente adivinhar.')
print('PENSANDO...')
sleep(5)
n = random.randint(0, 5)
n1 = int(input('Insira o número que você acha:'))
if n1 == n:
    print('Parabéns, você acertou!!!')
else:
    print('Você errou lol !!!!!')
print('O número o qual pensei era {}'.format(n))
