while True:
    valores = []
    for cont in range(0, 5):
        valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    print(f'Você digitou os valores: {valores}')
    # utilizar o comando max() para saber o maior número e criamos uma variavel para ele:
    maior_valor = max(valores)
    menor_valor = min(valores)
    print('-=-' * 20)
    print(f'O maior valor digitado foi {maior_valor} nas posições', end=' ')
    for c in range(0, len(valores)):
        if maior_valor == valores[c]:
            print(c, end='..')
    print(f'\nO menor valor digitado foi {menor_valor} nas posições', end=' ')
    for c in range(0, len(valores)):
        if menor_valor == valores[c]:
            print(c, end='..')
    print()
    print('-=-' * 20)
    opcao = str(input('Deseja repetir o programa? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('FIM DO PROGRAMA')
