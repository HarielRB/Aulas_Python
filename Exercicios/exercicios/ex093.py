print('Analisador de aproveitamento de jogadores')
dados = {}
cont = 0
numero_gols = []
dados['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Insira o número de partidas que o jogador {dados["Nome"]} jogou: '))
for p in range(1, partidas + 1):
    gols = int(input(f'Gols marcados na {p} partida: '))
    numero_gols.append(gols)
    cont += gols
dados['Gols'] = numero_gols[:]
dados['Total'] = cont
# poderia utilizar o comando sum(numero_gols)
print('-=-' * 20)
for k, v in dados.items():
    print(f'No slot {k} temos o valor {v}')
print('-=-' * 20)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas no total.')
for i, v in enumerate(numero_gols):
    print(f' => Na partida {i} ele marcou {v} gols.')
print(f'Foi um total de {dados["Total"]}')
print('-=-' * 20)
