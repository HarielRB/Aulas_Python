print('IDENTIFICADOR DE VOGAIS EM PALAVRAS DENTRO DE UMA TUPLA')
palavras = ('ABACO', 'TUCANO')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end=" ")
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
print('\nFIM')
