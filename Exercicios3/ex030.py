from time import sleep
print('Sistema de aprovação Escola Y')
nome = str(input('Insira o nome do aluno: ')).strip().upper()
nota_1 = float(input('Insira sua primeira nota: '))
nota_2 = float(input('Insira sua segunda nota: '))
media = (nota_1 + nota_2) / 2
if 10 >= media >= 9:
    letra = 'A'
elif 9 > media >= 7.5:
    letra = 'B'
elif 7.5 > media >= 6:
    letra = 'C'
elif 6 > media >= 4.0:
    letra = 'D'
else:
    letra = 'D'
print('\033[1;35m''CALCULANDO...''\033[m')
sleep(3)
print('ALUNO: {} '.format(nome))
print('Média: {:.2f} '.format(media))
print('Média literal: {} '. format(letra))
colecao = ['A', 'B', 'C']
if letra in colecao:
    print('\033[1;34m''APROVADO''\033[m')
else:
    print('\033[1;31m''REPROVADO')
