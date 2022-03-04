print('Indentificador de PARES E IMPARES')
num_par = 0
num_impar = 0
c = 0
for c in range(1, 11):
    num = int(input('Insira o {} número: '.format(c)))
    if num % 2 == 0:
        num_par = num_par + 1
    else:
        num_impar = num_impar + 1
    c = c + 1
print('Você digitou {} valores.'.format(c))
print('Números pares: {}'.format(num_par))
print('Números impares: {}'.format(num_impar))
