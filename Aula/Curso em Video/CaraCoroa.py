import random
print('Lançarei uma moeda')
nome1 = str(input('Insira o nome do primeiro jogador:')).strip()
nome2 = str(input('Insira o nome do segundo jogador:')).strip()
escolha1 = str(input('Sua escolha {}:'.format(nome1))).strip()
escolha2 = str(input('Sua escolha {}:'.format(nome2))).strip()
print('A moeda caiu com a face {} virada para cima'.format(random.choice([escolha1, escolha2])))
