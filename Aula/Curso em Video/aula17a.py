valores = []
"""valores.append(5)
valores.append(9)
valores.append(4)"""
# para adicionarmos os valores em uma lista:
for cont in range(0, 5):
    valores.append(int(input('Insira um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
