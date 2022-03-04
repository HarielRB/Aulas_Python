print('-=-' * 20)
print('FESTA DA DEMOCRACIA')
print('ELEIÇÔES CONSELHO')
print('-=-' * 20)
limite = int(input('Insira a quantidade de Eleitores: '))
hokage = 0
rei_mago = 0
kira = 0
for c in range(1, limite + 1):
    print('-=-' * 20)
    print('LLISTA DE CANDIDATOS')
    print('[ 1 ] Rei Mago')
    print('[ 2 ] Kira')
    print('[ 3 ] Hokage')
    print('-=-' * 20)
    voto = str(input('Inisra o número de seu candidato: ')).strip()
    if voto not in '123':
        print('\033[1;31m''OPÇÃO INVÁLIDA''\033[m')
        while voto not in '123':
            voto = str(input('Insira o número de seu candidato: ')).strip()
    if voto == '1':
        rei_mago += 1
    elif voto == '2':
        kira += 1
    else:
        hokage += 1
    print('Voto computado com sucesso')
    c += 1
print('REUNINDO VOTOS.....')
print(f'CANDIDATO 1: {rei_mago}')
print(f'CANDIDATO 2: {kira}')
print(f'CANDIDATO 3: {hokage}')
