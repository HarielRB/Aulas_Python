print('Calculadora de médias')
num = 0
soma = 0
divisor = 0
contador = 1
while num != 'SAIR':
    num = input('Insira a {} nota ou digite SAIR para encerrar: '.format(contador)).strip().upper()
    if num != 'SAIR':
        soma += float(num)
        divisor += 1
        contador += 1
media = soma / divisor
print('A média entre essas notas corresponde á: {:.2f}'.format(media))
