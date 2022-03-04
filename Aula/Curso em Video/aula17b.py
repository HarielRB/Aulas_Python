a = [1, 2, 3, 4]
# b = a
# b[2] = 8
# quando é criada uma igualdade entre listas, o python cria uma ligação entre elas
# para fazer com que b receba uma copia de A escrevemos assim:
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
