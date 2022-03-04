print('Matriz 2.0')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
terceira = 0
for c in range(0, 3):
    for p in range(0, 3):
        matriz[c][p] = int(input(f'Insira um número para a posição [{c}, {p}]: '))
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end='')
        if p == 2:
            print()
            terceira += matriz[c][p]
        if matriz[c][p] % 2 == 0:
            soma += matriz[c][p]
print(f'A soma entre todos os números pares corresponde á {soma}')
print(f'A soma dos valores da terceira coluna corresponde á {terceira}')
print(f'O maior valor da segunda linha corresponde á {max(matriz[1])}')
