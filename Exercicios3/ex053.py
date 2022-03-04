print('Identificador de faixa etária de um grupo')
num = 0
soma = 0
divisor = 0
contador = 1
while True:
    num = input('Insira a idade da {} pessoa ou digite SAIR para encerrar: '.format(contador)).strip().upper()
    if num == 'SAIR':
        break
    else:
        soma += int(num)
        divisor += 1
        contador += 1
media = soma / divisor
print('A media da idade entre {} pessoas é igual á {} anos.'.format(divisor, media))
if media < 25:
    grupo = 'JOVEM'
elif 60 > media >= 26:
    grupo = 'ADULTO'
else:
    grupo = 'IDOSO'
print('Seu grupo é classificado como {} .'.format(grupo))
