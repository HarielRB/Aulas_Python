from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
c = 1
cont = 1
input()
for k, v in dados.items():
    print(f' O {k} tirou no dado o valor {v}')
    sleep(1)
print('---' * 20)
print('Ordem de Vencedores')
raking = {}
# há a necessidade de utilizarmos a função itemgetter juntamente com o comando sorted
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
# o valor 1 especificado no parentese do itemgetter diz respeito ao indice dos valores que queremos utilizar como parame
# tro para organização, para invertermos a ordem de apresentação utilizaremos o reverse=True
for k, v in enumerate(ranking):
    # o dicionário se tranforma em uma lista, por isso devemos utilizar o comando enumerate
    print(f'{k + 1}° lugar: {v[0]} valor {v[1]} ')
