def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) na carreira')


# programa principal
n = str(input('Digite o nome do jogador: ')).strip().capitalize()
g = input('Insira a quantidade de gols do jogador: ')
if g.isnumeric():
    g = int(g)
    # ler o G como uma string e caso ele seja numerico, transforma-lo em inteiro
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
