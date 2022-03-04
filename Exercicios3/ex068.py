print('Eleiçõs Babacas 2020')
print('[ 1 ]  Paulinho Antunes')
print('[ 2 ]  Armando Pinto')
print('[ 3 ]  Zézinho')
print('[ 4 ]  Lurdinho')
print('[ 5 ]  Voto Nulo')
print('[ 6 ]  Voto em Branco')
paulinho = 0
armando = 0
zezinho = 0
lurdinho = 0
nulo = 0
branco = 0
contador = 0
while True:
    voto = int(input(' Digite o númerop de seu candidato: '))
    if voto == 0:
        break
    else:
        contador += 1
        if voto == 1:
            paulinho += 1
        elif voto == 2:
            armando += 1
        elif voto == 3:
            zezinho += 1
        elif voto == 4:
            lurdinho += 1
        elif voto == 6:
            branco += 1
        else:
            nulo += 1
print('---' * 20)
print(f'{"Contagem de votos":^60}')
print('---' * 20)
print(f'{"Paulinho Antunes:":^17} {paulinho:^10}')
print(f'{"Armando Pint0:":17} {armando:^10}')
print(f'{"Zézinho:":17} {zezinho:^10}')
print(f'{"Lurdinho:":17} {lurdinho:^10}')
print(f'{"Votos Nulos:":17} {nulo:^10}')
print(f'{"Votos em Branco:":17} {branco:^10}')
print('---' * 20)
if contador > 0:
    porcentagem_nulo = (nulo * 100) / contador
    porcentagem_branco = (branco * 100) / contador
    print(f'{"% Votos Nulos:":17}{porcentagem_nulo:^14.2f}')
    print(f'{"% Votos Brancos:":17}{porcentagem_branco:^14.2f}')
