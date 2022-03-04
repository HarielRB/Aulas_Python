dados = {}
jogadores = []
print('Analisador de jogadores de Futebol 2.0')
while True:
    dados.clear()
    cont_gols = 0
    numero_de_gols = []
    print('===' * 20)
    dados['Nome'] = str(input('Nome: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas o jogador {dados["Nome"]} jogou ?  '))
    for p in range(1, partidas + 1):
        gol = int(input(f'Gols marcados na {p} partida: '))
        cont_gols += gol
        numero_de_gols.append(gol)
    dados['Gols'] = numero_de_gols[:]
    dados['Total'] = cont_gols
    jogadores.append(dados.copy())
    opcao = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('===' * 20)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for i, individuo in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for dados in individuo.values():
        print(f'{str(dados):<15}', end='')
    print()
print('===' * 20)
while True:
    jogador = input('Informe o codigo do Jogador para ver seus dados (SAIR para encerrar): ').strip().upper()
    while int(jogador) >= len(jogadores):
        jogador = input('Informe o codigo do Jogador para ver seus dados (SAIR para encerrar): ').strip().upper()
    if jogador == 'SAIR':
        break
    else:
        print(f'-- Levantamendo do jogador {jogadores[int(jogador)]["Nome"]}')
        for p, g in enumerate(jogadores[int(jogador)]['Gols']):
            # enumerate utilizado pois o indice Gols é composto por uma lista
            print(f'Na partida {p} ele marcou {g} gols.')
print('Programa encerrado.')
