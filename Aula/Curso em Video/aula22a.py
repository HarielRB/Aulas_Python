def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Insira um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} corresponde a {fat}')
