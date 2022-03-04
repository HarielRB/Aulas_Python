def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# programa principal
n = int(input('Insira um número para o cálculo de seu fatorial: '))
print(f'O fatorial de {n} corresponde á {fatorial(n)}')
