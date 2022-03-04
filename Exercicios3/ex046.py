print('-=-' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 20)
termo = int(input('Quantos termos você deseja ver ? '))
contador = 0
print('~~' * 30)
t1 = 0
t2 = 1
print('{} → {} →'.format(t1, t2), end=' ')
while contador <= termo:
    contador = contador + 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} → '.format(t3), end='')
print('FIM')
print('~~' * 30)
