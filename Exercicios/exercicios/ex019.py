import random
print('Sorteie o nome do cachorro mais chato!!')
n1 = input('Primeiro nome:')
n2 = input('Segundo nome:')
n3 = input('Terceriro nome:')
n4 = input('Quarto nome:')
r = random.choice([n1, n2, n3, n4])
print('O escolhido foi você {}\n Parabéns, você é o mais chato da casa!'.format(r))
# poderia ser criado uma variavél de lista no exercicio
# l = [n1, n2, n3, n4]
