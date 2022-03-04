nome = str(input('Digite seu nome completo:')).strip()
ma = nome.upper()
mi = nome.lower()
nome1 = nome.split()
n1 = len(nome1[0])
n2 = len(nome) - nome.count(' ')
# n2 = len(''.join(l))
print('Analisando seu nome...')
print('-' * 12)
print('Seu nome em maiusculo se escreve: {} \n Seu nome em minusculo se escreve: {}\n'
      'Ao total seu nome possui {} letras; \n'
      'Seu primeiro nome possui {} letras'.format(ma, mi, n2, n1))
# para descobrir quantas letras o nome possui, devemos contar o total de caracteres e subtrair os espaços
