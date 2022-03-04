valores = []
while True:
    num = input('Digite um valor(SAIR para encerrar): ').strip().upper()
    if num == 'SAIR':
        break
    elif int(num) not in valores:
        valores.append(int(num))
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não será adicionado')
valores.sort()
print('-=-' * 20)
print(f'Você digitou os valors: {valores}')
