print('Análise de aprovação.')
nota_1 = float(input('Insira a primeira nota:'))
nota_2 = float(input('Insira a segunda nota:'))
media = (nota_1 + nota_2) / 2
print('A média desse aluno foi {:.2f}'.format(media))
if media < 5.00:
    print('\033[1;31m''ALUNO REPROVADO''\033[m')
elif 7 > media >= 5.00:
    print('\033[1;33m''ALUNO EM RECUPERAÇÃO''\033[m')
elif 10 >= media >= 7:
    print('\033[1;32m''ALUNO APROVADO''\033[m')
else:
    print('Média inválida')
