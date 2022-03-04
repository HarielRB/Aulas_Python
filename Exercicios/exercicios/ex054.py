from datetime import date
print('Identificador de maior idade')
menor_de_idade = 0
maior_de_idade = 0
for c in range(1, 8):
    ano = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior_de_idade = maior_de_idade + 1
    else:
        menor_de_idade = menor_de_idade + 1
        # O +1 foi utilizado para adicionar um número de aparições de pessoas
        # cada aparição é +1 e nao C pois ele corresponde a posição
print('{} pessoas entre vocês ja são maiores idade'.format(maior_de_idade))
print('E {} pessoas são menores de idade'.format(menor_de_idade))
