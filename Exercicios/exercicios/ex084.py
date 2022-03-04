populacao = []
pessoas = []
maior = 0
menor = 0
cont = 0
# peso_lista = []
while True:
    nome = str(input('Nome: ')).strip().upper()
    while not nome.isalpha():
        nome = str(input('Nome: ')).strip().upper()
    peso = float(input('Peso:KG '))
    pessoas.append(nome)
    pessoas.append(peso)
    # peso_lista.append(peso)
    populacao.append(pessoas[:])
    if cont == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if menor > pessoas[1]:
            menor = pessoas[1]
    pessoas.clear()
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'Foram cadastrados {len(populacao)} pessoas.')
# maior_peso = max(peso_lista)
print(f' O maior peso encontrado foi de {maior} KG. Os nomes são ', end='')
for p in populacao:
    if p[1] == maior:
        print(p[0], end=' ')
# menor_peso = min(peso_lista)
print()
print(f'O menor peso encontrado foi de {menor} KG. Os nomes são ', end='')
for c in populacao:
    if c[1] == menor:
        print(c[0], end=' ')
