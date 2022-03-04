print('Indentificador de pesos')
# criar duas variaveis iguais a 0
maiorp = 0
menorp = 0
for c in range(1, 6):
    peso = float(input('Insira o peso da {}ª pessoa: KG '.format(c)))
    # adicionar agora uma condição para considerar o primeiro valor como maior e menor
    if c == 1:
        maiorp = peso
        menorp = peso
        # quando digitarmos o primeiro valor, ele será considerado como o maior e o menor pois não ha comparativo
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O maior peso é {}Kg' .format(maiorp))
print('O menor peso é {}KG'.format(menorp))
# Busquei ajuda nos videos de resolução
# Quando quiser identificar qual e maior ou menor, deve-se verificar se foi a primeira ocorrencia
