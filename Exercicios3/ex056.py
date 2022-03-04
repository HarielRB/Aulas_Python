print('Média de alunos por turma')
alunos = int(input('Insira o número de alunos: '))
turma = int(input('Insira quantas turmas são desejadas: '))
while alunos >= 40:
    alunos -= 40
    turma += 1
print(turma)