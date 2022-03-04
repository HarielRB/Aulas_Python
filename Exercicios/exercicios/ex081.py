valores = []
cont = 0
while True:
    num = input('Digite um número (sair para encerrar): ').strip().upper()
    if num == 'SAIR':
        break
    else:
        cont += 1
        valores.append(int(num))
valores.sort(reverse=True)
print('-=-' * 20)
print(f'Você digitou {cont} Valores ao total')
print(f'Essa é a ordem decrescente dos valores: {valores} ')
if 5 in valores:
    posicao_5 = []
    cont_5 = 0
    for pos in range(0, len(valores)):
        if valores[pos] == 5:
            posicao_5.append(pos)
            cont_5 += 1
    print(f'O valor 5 foi digitado {cont_5} vezes nas posições {posicao_5}')
else:
    print('O valor 5 não foi digitado')
