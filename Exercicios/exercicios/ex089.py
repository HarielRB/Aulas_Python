from time import sleep
alunos = []
while True:
    nome = str(input('Nome: '))
    while not nome.isalpha():
        nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1 :'))
    nota_2 = float(input('Nota 2 : '))
    media = (nota_1 + nota_2) / 2
    alunos.append([nome, [nota_1, nota_2], media])
    continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-' * 26)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":>8}')
for indice, aluno in enumerate(alunos):
    print(f'{indice + 1:<5}{aluno[0]:<15}{aluno[2]:>8.2f}')
while True:
    num_aluno = int(input('De qual aluno você gostaria de conferir as notas (999 para encerrar)? '))
    if num_aluno == 999:
        print('ENCERRANDO PROCESSOS...')
        sleep(1.5)
        break
    else:
        print(f'O/A aluno(a) {alunos[num_aluno - 1][0]} apresentou as notas {alunos[num_aluno - 1][1]}')
        if alunos[num_aluno - 1][2] < 6:
            print('\033[1;31m''ALUNO REPROVADO''\033[m')
        else:
            print('\033[1;32m''ALUNO APROVADO''\033[m')
print('Até mais....')