from time import sleep
aluno = {}
aluno['Nome'] = str(input('Digite o nome do(a) Aluno(a): ')).strip()
aluno['Média'] = float(input(f'Digite a média do(a) {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print('ANALISANDO....')
sleep(1.5)
for k, v in aluno.items():
    print(f'{k} é {v}')
