brasil = []
estado = {}
for c in range(0, 3):
    estado['estado'] = str(input('Digite o nome do estado: ')).strip().upper()
    estado['uf'] = str(input('Digite a sigla do estado: ')).strip().upper()
    while len(estado['uf']) > 2:
        estado['uf'] = str(input('Digite a sigla do estado novamente: ')).strip().upper()
    brasil.append(estado.copy())
    print('---' * 10)
    # em dicionários não podemos realizar o fatiamento
# print(brasil)
print(f'{"Estado":^10}')
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
