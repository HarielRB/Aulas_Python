import random
from time import sleep
print('\033[35m''-=-' * 20)
print('\033[34m''Jokenpô contra o computador')
print('\033[35m''-=-''\033[m' * 20)
print('Vamos lá')
colecao = ['PEDRA', 'PAPEL', 'TESOURA']
opcao_pc = random.choice(colecao)
print('Eu ja escolhi')
opcao_j = str(input('O que você vai jogar?')).strip().upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if opcao_j == opcao_pc:
    print('\033[1;36m' 'EMPATAMOS''\033[m')
elif opcao_j == 'PEDRA' and opcao_pc == 'TESOURA' or opcao_j == 'PAPEL' and opcao_pc == 'PEDRA' or \
        opcao_j == 'TESOURA' and opcao_pc == 'PAPEL':
    print('\033[32m''Você ganhou''\033[m')
else:
    print('\033[31m''Eu ganhei, você perdeu''\033[m')
print('Eu escolhi {}'.format(opcao_pc))
wait = input('Pressione uma tecla:')
