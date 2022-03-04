valores = []
valores_pares = []
valores_impares = []
while True:
    num = input('Digite um número (sair para encerrar): ').strip().upper()
    if num == 'SAIR':
        break
    else:
        valores.append(int(num))
for cont in range(0, len(valores)):
    if valores[cont] % 2 == 0:
        valores_pares.append(valores[cont])
    else:
        valores_impares.append(valores[cont])
print(f'Valores digitados ao todo: {valores}')
print(f'Valores pares: {valores_pares}')
print(f'Valores impares: {valores_impares}')
