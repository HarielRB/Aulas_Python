print('Calculadora de soma')
n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Insira um número [999 para parar]: '))
    if n != 999:
        # quando o número inserido for 999 a condição não será sanada, logo o programa irá sair da repetição
        soma = soma + n
        c = c + 1
print('A soma desses {} números é igual a {}'.format(c, soma))
# poderia colocar o input do lado de fora do laço e um dentro em vez de usar o if
