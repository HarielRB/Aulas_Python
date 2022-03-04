from random import randint
""" maior = 0
menor = 0
print('Número gerados aleatoriamente: ', end=' ')
for c in range(1, 6):
    num = randint(0, 10)
    print(num, end=' ')
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'\nO maior número foi {maior}')
print(f'O menor número foi {menor}') """
num_1 = randint(1, 10)
num_2 = randint(1, 10)
num_3 = randint(1, 10)
num_4 = randint(1, 10)
num_5 = randint(1, 10)
conjunto = (num_1, num_2, num_3, num_4, num_5)
print('Valores sorteados: ', end=' ')
for c in conjunto:
    print(c, end=' ')
# existe um método para tuplas que apresenta o maior valor dentro dela
# esse valor é o Max()
print(f'\nO maior valor sorteado foi {max(conjunto)}')
# existe também o metodo min o qual apresenta o menor valor dentro ta tupla
print(f'O menor valor sorteado foi {min(conjunto)}')
