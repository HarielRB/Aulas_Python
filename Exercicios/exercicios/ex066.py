from time import sleep
print('Soma de diversos números')
contador = 0
soma = 0
while True:
    num = int(input('Insira um número (999 para sair): '))
    if num == 999:
        break
    soma += num
    contador += 1
print('CALCULANDO....')
sleep(0.5)
print(f'Foram digitados {contador} números.')
print(f'A soma entre eles corresponde à {soma}')
# exercicio correto
