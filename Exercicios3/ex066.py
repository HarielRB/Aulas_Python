print('Identificador de números')
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0
while True:
    num = int(input('Insira um número : '))
    if num < 0:
        break
    else:
        if 25 >= num >= 0:
            intervalo_1 += 1
        elif 50 >= num >= 16:
            intervalo_2 += 1
        elif 75 >= num >= 51:
            intervalo_3 += 1
        else:
            intervalo_4 += 1
print(f'Números entre 0 e 25: {intervalo_1}')
print(f'Númeroes entre 26 e 50: {intervalo_2}')
print(f'Números entre 51 e 75: {intervalo_3}')
print(f'Números entre 76 e 100: {intervalo_4}')
