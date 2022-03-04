from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
dados['Idade'] = idade
dados['CTPS'] = int(input('Carteira de trabalho (0 caso não possua): '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    while dados['Contratação'] <= nascimento:
        print('Ano de contratação invalido, digite novamente.')
        dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    idade_aposentadoria = dados['Contratação'] + 35 - nascimento
    dados['Aposentadoria'] = idade_aposentadoria
for k, v in dados.items():
    print(f'-> {k}: {v}')
