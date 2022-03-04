cont_idade = 0
cont = 0
cont_mulheres = 0
dados = {}
grupo = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip().capitalize()
    dados['Sexo'] = str(input('Sexo: [F/M] ')).strip().upper()
    while dados['Sexo'] not in 'FM':
        dados['Sexo'] = str(input('Digite o sexo novamente: [F/M] ')).strip().upper()
    if dados['Sexo'] == 'F':
        cont_mulheres += 1
    idade = int(input('Idade: '))
    dados['Idade'] = idade
    grupo.append(dados.copy())
    cont_idade += idade
    cont += 1
    continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção invalida. Deseja continuar ? '))
    if continuar == 'N':
        break
print('===' * 30)
print(f' -> O grupo tem {cont} pessoas')
media = cont_idade / cont
print(f' -> A média de idade do grupo é igual a {media:.2f}')
if cont_mulheres > 0:
    print(f' -> As mulheres cadastradas são: ')
    for individuos in grupo:
        if individuos['Sexo'] == 'F':
            print(individuos['Nome'])
    print()
print(' -> Lista das pessoas que estão acima da média: ')
for individuos in grupo:
    if individuos['Idade'] > media:
        for k, v in individuos.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< ENCERRADO >> ')
