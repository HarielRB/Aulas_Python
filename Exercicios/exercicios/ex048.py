""" s = 0
linhas = 0
for c in range(3, 501, 3):
    s = s + c
    print(c)
    if c % 3 == 0:
        linhas = linhas + 1
print('.')
print(' A soma entre esses {} valores corresponde  a {}'.format(linhas, s) """
# programa está excluindo 30 e seus multiplos
# foi efetuada a correção
# correção
soma = 0
linhas = 0
for c in range(1, 501, 2):
    # apresentando apenas os números ímpares
    if c % 3 == 0:
        # condição adicionada para apresentar apénas os multiplos de 3
        print(c)
        soma = soma + c
        linhas = linhas + 1
print('A soma desses {} valores corresponde a {}.'.format(linhas, soma))
