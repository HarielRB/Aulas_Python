matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('Gerador de matriz')
for indice in range(0, 3):
    for elemento in range(0, 3):
        matriz[indice][elemento] = int(input(f'Digite um número para a posição [{indice}, {elemento}]: '))
print('-=-' * 20)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end='')
        if p == 2:
            print()
