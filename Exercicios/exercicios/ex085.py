numeros = [[], []]
for c in range(1, 8):
    num = int(input(f'Insira o {c}° número: '))
    if num % 2 == 0:
        # para inserir um numéro numa posiçao específica de uma lista composta colocamos a lista com seu indice.append
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Voce digitou os números {numeros}')
print(f'Os números pares foram: {numeros[0]}')
print(f'Os números impares foram: {numeros[1]}')
