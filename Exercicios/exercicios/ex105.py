def notas(*n, sit=False):
    """ --> Função para analisar notas, média e situação de alunos
        :param n: valores das notas a serem calculadas
        :param sit: (opcional) indica se a situação deve ou não ser adicionada
        :return: dicionario contendo as informações desejadas"""
    aluno = dict()
    aluno['Quantidade de Notas'] = len(n)
    aluno['Maior Nota'] = max(n)
    aluno['Menor Nota'] = min(n)
    media = sum(n) / len(n)
    aluno['Média'] = media
    if sit:
        if media < 5:
            aluno['Situação'] = 'RUIM'
        elif 7 >= media >= 5:
            aluno['Situação'] = 'ATENÇÃO'
        else:
            aluno['Situação'] = 'BOM'
    return aluno


# programa principal
resp = notas(5, 4, 2, 10, 5.5, sit=True)
print(resp)
resp = notas(5, 3.2, 8.9, 10, sit=True)
print(resp)
resp = notas(2, 1, 8, 9, 10, 5.5, 7.5)
print(resp)
