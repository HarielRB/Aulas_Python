times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Lista de times do Brasileirão 2019: {times}')
print(f'Os 5 primeiros colocados são {times[:5]}')
print(f'Os 4 ultimos são: {times[-4:]}')
print(f'A ordem alfabética dos times é : {sorted(times)} ')
# o comando sorted transforma a tupla em orde, porem ela é printada em forma de lista
print('O Chapecoense está na {}ª posição da tabela'.format(times.index('Chapecoense') + 1))
