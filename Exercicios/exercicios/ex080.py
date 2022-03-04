valores = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        # até esse passo a logica estava certa, depois disso o programa estava apresentando bugs
        print('Número adicionado ao final da lista.')
    else:
        posicao = 0
        # devemos criar uma variavel de posição e colocarmos em um laço
        while posicao < len(valores):
            # criamos um laço para que ele verifique a posição em relaação ao tamanho da lista
            if valores[posicao] >= num:
                # se o valor contido na posição for maior que o num adicionamos onumnessaposição
                valores.insert(posicao, num)
                print(f'O valor foi adicionado na posição {posicao}')
                break
            posicao += 1
            # soma utilizada para nos levar para a proixma posiçao
print('-=-' * 20)
print(f'Os valores digitados em ordem crescente foram: {valores}')
