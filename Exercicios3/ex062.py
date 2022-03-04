print('Senso Academia XYZ')
contador = 0
maior_peso = 0
menor_peso = 0
mais_alto = 0
mais_baixo = 0
cod_ma = ''
cod_mb = ''
cod_mp = ''
cod_mep = ''
soma_altura = 0
soma_peso = 0
while True:
    codigo = str(input('Insira seu código de Mátricula (0 para encerrar): ')).strip()
    if codigo == '0':
        break
    else:
        contador += 1
        peso = float(input('Insira seu peso (KG): '))
        altura = float(input('Insira sua altura (metros): '))
        soma_altura += altura
        soma_peso += peso
        if contador == 1:
            maior_peso = peso
            menor_peso = peso
            mais_alto = altura
            mais_baixo = altura
            cod_ma = cod_mb = cod_mp = cod_mep = codigo
        if peso > maior_peso:
            maior_peso = peso
            cod_mp = codigo
        if peso < menor_peso:
            menor_peso = peso
            cod_mep = codigo
        if altura > mais_alto:
            mais_alto = altura
            cod_ma = codigo
        if altura < mais_baixo:
            mais_baixo = altura
            cod_mb = codigo
print(f'Maior peso: {maior_peso} Código do aluno: {cod_mp}')
print(f'Menor Peso: {menor_peso} Código do aluno: {cod_mep}')
print(f'Aluno mais baixo: {cod_mb}, altura {mais_baixo}')
print(f'Aluno mais alto: {cod_ma}, altura {mais_alto}')
print(f'A média de tamanho da academia é de : {soma_altura / contador:.2f}')
print(f'A média de peso da academia é de: {soma_peso / contador:.2f}')
