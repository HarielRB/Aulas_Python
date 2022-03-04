from time import sleep
print('Calculadora de Média Escolar')
n1 = float(input('Insira a Primeira Nota:'))
n2 = float(input('Insira a Segunda Nota: '))
n3 = float(input('Insira a Terceira Nota:'))
n4 = float(input('Insira a Quarta Nota:'))
print('-~-' * 20)
print('Calculando...')
print('-~-' * 20)
sleep(5)
m = (n1 + n2 + n3 + n4) / 4
print('A soma de suas notas corresponde a {:.2f}.'.format(m))
mf = float(input('Insira a média para aprovação:'))
if m >= mf:
    print('Parabéns, você foi aprovado!')
else:
    print('Sentimos muito, você reprovou.')
