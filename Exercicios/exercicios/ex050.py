print('Calculadora apenas de números pares')
s = 0
pares = 0
for c in range(1, 7):
    num = float(input('Insira o {} º número: '.format(c)))
    if num % 2 == 0:
        s = s + num
        pares = pares + 1
print('Você informou {} números pares e a soma deles foi {}'.format(pares, s))
