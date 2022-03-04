print('Calculadora de soma')
num = 0
contador = 0
soma = 0
maior = 0
menor = 0
while num != 1001:
    contador += 1
    num = int(input('Insira o {}  número entre 0 e 1000 [1001 para parar]: '.format(contador)))
    if num != 1001:
        if contador == 1:
            maior = num
            menor = num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
print('Foram digitados {} valores'.format(contador - 1))
print('SOMA: {}'.format(soma))
print('MAIOR VALOR DIGITADO: {}'.format(maior))
print('MENOR VALOR DIGITADO: {}'.format(menor))
