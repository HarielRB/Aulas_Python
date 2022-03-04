print('SEQUENCIA DE FIBONACCI')
print('Irei te mostrar a sequencia até que ela chegue em 500')
t1 = 0
t2 = 1
print('{} → {} →'.format(t1, t2), end=' ')
t3 = t1 + t2
contador = 0
while t3 < 500:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    contador += 1
    print('{} →'.format(t3), end=' ')
print('FIM')
print('Foram necessários {} termos'.format(contador))