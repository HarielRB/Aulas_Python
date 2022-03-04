print('Igualador de populações')
opcao = 'S'
while opcao == 'S':
    a = int(input('Insira a população da primeira cidade: '))
    taxa_a = float(input('Insira a taxa de crescimento da primeira cidade: % '))
    taxa_real_a = taxa_a / 100
    b = int(input('Insira a população da segunda cidade: '))
    taxa_b = float(input('Insira a taxa de crescimento da segunda cidade: %'))
    taxa_real_b = taxa_b / 100
    anos = 0
    if a < b:
        while a < b:
            a = a + (a * taxa_real_a)
            b = b + (b * taxa_real_b)
            anos = anos + 1
    else:
        while b < a:
            a = a + (a * taxa_real_a)
            b = b + (b * taxa_real_b)
            anos = anos + 1
    print('Levará {} anos para que a populações sejam iguais'.format(anos))
    opcao = str(input('Deseja realizar novos calculos [S/N]? ')).strip().upper()
print('Até mais')
