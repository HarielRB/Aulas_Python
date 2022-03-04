print('Identifacor de autura de alunos')
maior_aluno = ''
menor_aluno = ''
maior_altura = 0
menor_altura = 0
for c in range(1, 11):
    aluno = input('Insira o número do aluno: ').strip()
    altura = int(input('Insira a altura em centimetros: '))
    if c == 1:
        maior_altura = altura
        menor_altura = altura
        menor_aluno = aluno
        maior_aluno = aluno
    else:
        if altura > maior_altura:
            maior_altura = altura
            maior_aluno = aluno
        if altura < menor_altura:
            menor_altura = altura
            menor_aluno = aluno
    c += 1

print(f'Aluno mais alto : {maior_aluno} , {maior_altura} cm')
print(f'Aluno mais baixo: {menor_aluno}, {menor_altura} cm')
print('FIM!')
