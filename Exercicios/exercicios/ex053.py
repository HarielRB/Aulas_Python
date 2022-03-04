print('Analisador de Palíndromos')
frase = str(input('Digite uma frase:')).strip().upper()
virgu = frase.replace(' ', '')
# poderia ter usado os comandos .split e .join
frase2 = virgu[::-1]
# o comando replace deve conter o caractere que sera substituido e o seu substituidor
if virgu == frase2:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase não é um Pàlíndromo')
