print('Identificador de maior e menor número')
c = 0
maior = 0
menor = 0
for c in range(1, 5):  # nao podemos comecar o range com 0 pois o programa irá levar em consideração o segundo número
    num = int(input('Insira um número: '))
    if c == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    c = c + 1
print('O menor número dentre esses {} números é {}'.format(c, menor))
print('O maior número dentre esses {} números é {}'.format(c, maior))
