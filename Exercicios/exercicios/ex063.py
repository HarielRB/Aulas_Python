print('-' * 25)
print('Sequência de FIBONACCI')
print('-' * 25)
termos = int(input('Quantos termos da sequência você deseja? '))
c = 0
# há a necessidade de criar duas variaveis: T1 e T2 que corresponderão aos termos
t1 = 0
t2 = 1
print('{} → {} →'.format(t1, t2), end=' ')
while c <= termos:
    # criaremos agora a variavel t3 que corresponde a soma de t1 e t2
    t3 = t1 + t2
    print(t3, end=' → ')
    # quando a soma for realizada devemos fazer com que o programa ande para frente logo igualamos
    t1 = t2
    t2 = t3
    # Devemos fazer isso para que os três valores "andem" para frente
    c = c + 1
print('FIM')
