import random
print('-=-' * 20)
print('PAR OU ÍMPAR')
print('-=-' * 20)
contador = 0
vencedor = 0
while True:
    contador += 1
    jogador_op = str(input('Qual sua escolha [I/P]? ')).strip().upper()
    while jogador_op not in 'PI':
        jogador_op = str(input('Qual sua escolha [I/P]? '))
    jogador_num = int(input('Digite o número: '))
    pc_num = random.randint(0, 10)
    soma = pc_num + jogador_num
    if soma % 2 == 0:
        winner = 'PAR'
    else:
        winner = 'IMPAR'
    print(f'Você jogou {jogador_num} e eu joguei {pc_num} a soma deu {soma} ou seja {winner} ')
    if jogador_op == winner[0]:
        print('Você venceu e eu PERDI.')
        vencedor += 1
    else:
        print('Eu ganhei e você PERDEU')
        break
    print('Vamos jogar novamente...')
print(f'Rodadas Jogadas: {contador} ')
print(f'Jogador venceu:  {vencedor} ')
print('Até Mais!!!')
