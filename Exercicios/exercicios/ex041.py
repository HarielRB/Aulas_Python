from datetime import date
from time import sleep
print('Classificação de Atletas de Natação')
ano = int(input('Insira seu ano de Nascimento:'))
idade = date.today().year - ano
print('\033[1;35m''ANALISANDO...''\033[m')
sleep(3)
if idade <= 9:
    categoria = '\033[32m''MIRIM''\033[m'
elif 14 >= idade:
    categoria = '\033[33m''INFANTIL''\033[m'
elif 19 >= idade:
    categoria = '\033[34m''JÚNIOR''\033[m'
elif 25 >= idade:
    categoria = '\033[36m''SÊNIOR''\033[m'
else:
    categoria = '\033[1;30m''MASTER''\033[m'
print('O atleta tem {} ano(s) de vida'.format(idade))
print('Sua categoria correspondente é {}'.format(categoria))
